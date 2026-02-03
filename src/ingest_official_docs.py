"""Crawl and ingest official documentation into ChromaDB"""
import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import argparse
from src.vectorstore import VectorStoreManager
from src.config import COLLECTIONS
from src.crawl_index import CrawlIndex
from src.crawlers import (
    DockerCrawler,
    KubernetesCrawler,
    TerraformCrawler,
    IstioCrawler,
    ArgoCDCrawler,
    AWSCrawler
)


def chunk_content(content: str, chunk_size: int = 1000, overlap: int = 200) -> list[str]:
    """Split content into overlapping chunks"""
    if len(content) <= chunk_size:
        return [content]
    
    chunks = []
    start = 0
    
    while start < len(content):
        end = start + chunk_size
        
        # Try to break at sentence boundary
        if end < len(content):
            # Look for sentence end
            for i in range(end, max(start + overlap, end - 200), -1):
                if content[i] in '.!?\n':
                    end = i + 1
                    break
        
        chunk = content[start:end].strip()
        if chunk:
            chunks.append(chunk)
        
        start = end - overlap
    
    return chunks


def ingest_crawler_documents(
    crawler, 
    collection_name: str, 
    vectorstore: VectorStoreManager,
    crawl_index: CrawlIndex,
    force_reindex: bool = False,
    batch_size: int = 10
):
    """Crawl and ingest documents from a crawler in batches"""
    print(f"\n{'='*60}")
    print(f"Processing {crawler.__class__.__name__}")
    print(f"{'='*60}")
    
    # Get start URLs
    start_urls = crawler.get_start_urls()
    
    # Check existing index
    if not force_reindex:
        processed_urls = set(crawl_index.get_processed_urls(collection_name))
        print(f"\n✓ Found {len(processed_urls)} already processed URLs")
        
        # Filter out processed URLs
        start_urls = [url for url in start_urls if url not in processed_urls]
        print(f"✓ {len(start_urls)} new URLs to crawl")
        
        if not start_urls:
            print("✓ All URLs already processed. Use --force to reindex.")
            return
    
    total_urls = len(start_urls)
    total_documents_processed = 0
    total_chunks_added = 0
    
    # Process in batches
    for batch_num, i in enumerate(range(0, total_urls, batch_size), 1):
        batch_urls = start_urls[i:i + batch_size]
        
        print(f"\n{'─'*60}")
        print(f"Batch {batch_num}/{(total_urls + batch_size - 1) // batch_size}")
        print(f"Processing URLs {i+1}-{min(i+batch_size, total_urls)} of {total_urls}")
        print(f"{'─'*60}")
        
        # Crawl batch (batch mode: don't follow links)
        print(f"Crawling {len(batch_urls)} URLs...")
        documents = crawler.crawl(batch_urls, follow_links=False)
        
        if not documents:
            print("✗ No documents found in this batch")
            continue
        
        print(f"✓ Crawled {len(documents)} documents")
        
        # Process and chunk documents
        batch_chunks = []
        batch_metadatas = []
        url_chunk_counts = {}
        
        for doc in documents:
            # Chunk content
            chunks = chunk_content(doc.content, chunk_size=1000, overlap=200)
            url_chunk_counts[doc.url] = len(chunks)
            
            for chunk_idx, chunk in enumerate(chunks):
                batch_chunks.append(chunk)
                batch_metadatas.append({
                    'url': doc.url,
                    'title': doc.title,
                    'doc_id': doc.doc_id,
                    'chunk_id': f"{doc.doc_id}_{chunk_idx}",
                    'chunk_index': chunk_idx,
                    'total_chunks': len(chunks),
                    **doc.metadata
                })
        
        # Ingest batch into ChromaDB
        print(f"Ingesting {len(batch_chunks)} chunks into {collection_name}...")
        vectorstore.add_documents(collection_name, batch_chunks, batch_metadatas)
        print(f"✓ Ingested {len(batch_chunks)} chunks")
        
        # Update index for this batch
        print("Updating crawl index...")
        for doc in documents:
            crawl_index.mark_processed(
                url=doc.url,
                collection=collection_name,
                num_chunks=url_chunk_counts[doc.url],
                metadata={
                    'title': doc.title,
                    'section': doc.metadata.get('section', 'general')
                }
            )
        print(f"✓ Index updated for {len(documents)} URLs")
        
        total_documents_processed += len(documents)
        total_chunks_added += len(batch_chunks)
        
        print(f"\n📊 Batch {batch_num} Summary:")
        print(f"   Documents: {len(documents)}")
        print(f"   Chunks: {len(batch_chunks)}")
        print(f"   Progress: {min(i+batch_size, total_urls)}/{total_urls} URLs")
    
    print(f"\n{'='*60}")
    print(f"✓ Processing Complete")
    print(f"{'='*60}")
    print(f"Total documents: {total_documents_processed}")
    print(f"Total chunks: {total_chunks_added}")


def main():
    parser = argparse.ArgumentParser(description='Crawl and ingest official documentation')
    parser.add_argument(
        '--service',
        choices=['docker', 'kubernetes', 'terraform', 'istio', 'argocd', 'aws', 'all'],
        default='all',
        help='Service to crawl (default: all)'
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='Force reindex all URLs (ignore existing index)'
    )
    parser.add_argument(
        '--stats',
        action='store_true',
        help='Show crawl statistics and exit'
    )
    parser.add_argument(
        '--clear',
        type=str,
        help='Clear index for specific service'
    )
    parser.add_argument(
        '--batch-size',
        type=int,
        default=10,
        help='Number of URLs to process per batch (default: 10)'
    )
    args = parser.parse_args()
    
    # Initialize
    vectorstore = VectorStoreManager()
    crawl_index = CrawlIndex()
    
    # Show stats
    if args.stats:
        print("\n" + "="*60)
        print("Crawl Index Statistics")
        print("="*60)
        stats = crawl_index.get_stats()
        print(f"\nTotal URLs indexed: {stats['total_urls']}")
        print("\nBy collection:")
        for coll_name, coll_stats in stats.get('collections', {}).items():
            print(f"  {coll_name}:")
            print(f"    URLs: {coll_stats['total_urls']}")
            print(f"    Chunks: {coll_stats['total_chunks']}")
        return
    
    # Clear index
    if args.clear:
        service_collections = {
            'docker': COLLECTIONS['docker'],
            'kubernetes': COLLECTIONS['kubernetes'],
            'terraform': COLLECTIONS['terraform'],
            'istio': COLLECTIONS['istio'],
            'argocd': COLLECTIONS['gitops'],
        }
        
        if args.clear in service_collections:
            collection = service_collections[args.clear]
            print(f"\nClearing index for {args.clear} ({collection})...")
            crawl_index.clear_collection(collection)
            print("✓ Index cleared")
        else:
            print(f"✗ Unknown service: {args.clear}")
        return
    
    crawlers = {
        'docker': (DockerCrawler(), COLLECTIONS['docker']),
        'kubernetes': (KubernetesCrawler(), COLLECTIONS['kubernetes']),
        'terraform': (TerraformCrawler(), COLLECTIONS['terraform']),
        'istio': (IstioCrawler(), COLLECTIONS['istio']),
        'argocd': (ArgoCDCrawler(), COLLECTIONS['gitops']),
        'aws': (AWSCrawler(), COLLECTIONS['aws']),
    }
    
    if args.service == 'all':
        services_to_crawl = crawlers.keys()
    else:
        services_to_crawl = [args.service]
    
    print("\n" + "="*60)
    print("Official Documentation Crawler")
    print("="*60)
    print(f"\nServices to crawl: {', '.join(services_to_crawl)}")
    print(f"Batch size: {args.batch_size} URLs per batch")
    if args.force:
        print("⚠️  Force reindex enabled - will reprocess all URLs")
    print("\nThis may take several minutes...")
    
    for service in services_to_crawl:
        crawler, collection = crawlers[service]
        try:
            ingest_crawler_documents(
                crawler, 
                collection, 
                vectorstore, 
                crawl_index, 
                args.force,
                args.batch_size
            )
        except Exception as e:
            print(f"\n✗ Error crawling {service}: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "="*60)
    print("Crawling complete!")
    print("="*60)
    
    # Show summary
    print("\nCollection summary:")
    for collection in vectorstore.list_collections():
        print(f"  - {collection}")
    
    print("\nCrawl index summary:")
    stats = crawl_index.get_stats()
    for coll_name, coll_stats in stats.get('collections', {}).items():
        print(f"  {coll_name}: {coll_stats['total_urls']} URLs, {coll_stats['total_chunks']} chunks")


if __name__ == "__main__":
    main()
