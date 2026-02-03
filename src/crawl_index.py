"""Crawl index management to track processed URLs"""
import json
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional


class CrawlIndex:
    """Manages crawled URL index to prevent duplicate processing"""
    
    def __init__(self, index_file: str = "crawl_index.json"):
        self.index_file = Path(index_file)
        self.index: Dict[str, Dict] = self._load_index()
    
    def _load_index(self) -> Dict[str, Dict]:
        """Load index from file"""
        if self.index_file.exists():
            with open(self.index_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def _save_index(self):
        """Save index to file"""
        with open(self.index_file, 'w', encoding='utf-8') as f:
            json.dump(self.index, f, indent=2, ensure_ascii=False)
    
    def _generate_url_hash(self, url: str) -> str:
        """Generate hash for URL"""
        return hashlib.md5(url.encode()).hexdigest()
    
    def is_processed(self, url: str, collection: str) -> bool:
        """Check if URL has been processed for a collection"""
        url_hash = self._generate_url_hash(url)
        
        if url_hash not in self.index:
            return False
        
        return collection in self.index[url_hash].get('collections', [])
    
    def mark_processed(
        self, 
        url: str, 
        collection: str, 
        num_chunks: int,
        metadata: Optional[Dict] = None
    ):
        """Mark URL as processed for a collection"""
        url_hash = self._generate_url_hash(url)
        
        if url_hash not in self.index:
            self.index[url_hash] = {
                'url': url,
                'collections': [],
                'first_crawled': datetime.now().isoformat(),
                'metadata': {}
            }
        
        entry = self.index[url_hash]
        
        if collection not in entry['collections']:
            entry['collections'].append(collection)
        
        entry['last_updated'] = datetime.now().isoformat()
        entry['metadata'][collection] = {
            'num_chunks': num_chunks,
            'crawled_at': datetime.now().isoformat(),
            **(metadata or {})
        }
        
        self._save_index()
    
    def get_processed_urls(self, collection: str) -> List[str]:
        """Get all processed URLs for a collection"""
        urls = []
        for url_hash, entry in self.index.items():
            if collection in entry.get('collections', []):
                urls.append(entry['url'])
        return urls
    
    def get_stats(self, collection: Optional[str] = None) -> Dict:
        """Get crawl statistics"""
        if collection:
            urls = self.get_processed_urls(collection)
            total_chunks = sum(
                entry['metadata'].get(collection, {}).get('num_chunks', 0)
                for entry in self.index.values()
                if collection in entry.get('collections', [])
            )
            return {
                'collection': collection,
                'total_urls': len(urls),
                'total_chunks': total_chunks
            }
        else:
            # Overall stats
            all_collections = set()
            for entry in self.index.values():
                all_collections.update(entry.get('collections', []))
            
            stats = {
                'total_urls': len(self.index),
                'collections': {}
            }
            
            for coll in all_collections:
                stats['collections'][coll] = self.get_stats(coll)
            
            return stats
    
    def remove_url(self, url: str, collection: Optional[str] = None):
        """Remove URL from index"""
        url_hash = self._generate_url_hash(url)
        
        if url_hash not in self.index:
            return
        
        if collection:
            # Remove from specific collection
            entry = self.index[url_hash]
            if collection in entry.get('collections', []):
                entry['collections'].remove(collection)
                if collection in entry.get('metadata', {}):
                    del entry['metadata'][collection]
            
            # Remove entry if no collections left
            if not entry.get('collections'):
                del self.index[url_hash]
        else:
            # Remove completely
            del self.index[url_hash]
        
        self._save_index()
    
    def clear_collection(self, collection: str):
        """Clear all URLs for a collection"""
        urls_to_remove = []
        
        for url_hash, entry in self.index.items():
            if collection in entry.get('collections', []):
                urls_to_remove.append(entry['url'])
        
        for url in urls_to_remove:
            self.remove_url(url, collection)
    
    def export_urls(self, collection: str, output_file: str):
        """Export processed URLs to file"""
        urls = self.get_processed_urls(collection)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for url in urls:
                f.write(f"{url}\n")
        
        print(f"✓ Exported {len(urls)} URLs to {output_file}")
