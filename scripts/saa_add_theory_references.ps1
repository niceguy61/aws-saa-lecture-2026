param(
  [switch]$WhatIf
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Read-TextFileUtf8NoBom([string]$path) {
  return [System.IO.File]::ReadAllText($path, [System.Text.UTF8Encoding]::new($false))
}

function Write-TextFileUtf8NoBom([string]$path, [string]$content) {
  [System.IO.File]::WriteAllText($path, $content, [System.Text.UTF8Encoding]::new($false))
}

function Get-NewLine([string]$content) {
  if ($content.Contains("`r`n")) { return "`r`n" }
  return "`n"
}

function Get-RelativePath([string]$fromDir, [string]$toPath) {
  $fromDirFull = [System.IO.Path]::GetFullPath($fromDir)
  $toPathFull = [System.IO.Path]::GetFullPath($toPath)

  if (-not $fromDirFull.EndsWith([System.IO.Path]::DirectorySeparatorChar)) {
    $fromDirFull = $fromDirFull + [System.IO.Path]::DirectorySeparatorChar
  }

  $fromUri = [System.Uri]::new($fromDirFull)
  $toUri = [System.Uri]::new($toPathFull)
  $rel = $fromUri.MakeRelativeUri($toUri).ToString()
  $rel = [System.Uri]::UnescapeDataString($rel)
  return $rel.Replace("\\", "/").Replace("/", "/")
}

function New-MarkdownLink([string]$label, [string]$urlOrPath) {
  if ([string]::IsNullOrWhiteSpace($label)) { throw "label is required" }
  if ([string]::IsNullOrWhiteSpace($urlOrPath)) { throw "urlOrPath is required" }
  return "[$label]($urlOrPath)"
}

function New-AwsDocsSearchUrl([string]$query) {
  if ([string]::IsNullOrWhiteSpace($query)) { throw "query is required" }
  $q = [System.Uri]::EscapeDataString($query.Trim())
  return "https://docs.aws.amazon.com/search/doc-search.html?searchQuery=$q"
}

function Get-FirstMarkdownH1([string]$content) {
  $lines = $content -split "\r?\n"
  foreach ($line in $lines) {
    if ($line -match "^\s*#\s+(.+?)\s*$") { return $Matches[1].Trim() }
  }
  return $null
}

function Get-TheorySlugTokens([string]$filePath) {
  $base = [System.IO.Path]::GetFileNameWithoutExtension($filePath)
  $slug = ($base -replace "^\d{2}-", "").Trim()
  if ([string]::IsNullOrWhiteSpace($slug)) { return @() }
  return $slug.Split("-", [System.StringSplitOptions]::RemoveEmptyEntries) | ForEach-Object { $_.Trim().ToLowerInvariant() }
}

function Add-UniqueLink(
  [System.Collections.Generic.List[hashtable]]$links,
  [string]$label,
  [string]$url
) {
  foreach ($x in $links) {
    if ($x.Url -eq $url) { return }
  }
  $links.Add(@{ Label = $label; Url = $url })
}

function Get-OfficialAwsDocsLinks([string]$filePath, [string]$content) {
  $tokens = Get-TheorySlugTokens -filePath $filePath
  $slug = ($tokens -join "-")
  $links = New-Object System.Collections.Generic.List[hashtable]

  $isBroadScan = $false
  if ($filePath -match "(?i)\\special-lectures\\") { $isBroadScan = $true }
  if ($tokens -contains "theory") { $isBroadScan = $true }
  if ($slug -eq "detection-services") { $isBroadScan = $true }

  $defs = @(
    @{ Id="iam"; Label="IAM User Guide"; Docs="https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html"; Search="AWS IAM"; Tokens=@("iam"); Regex=@("\bIAM\b") },
    @{ Id="sts"; Label="STS API Reference"; Docs="https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html"; Search="AWS STS AssumeRole"; Tokens=@("sts"); Regex=@("\bSTS\b","AssumeRole") },
    @{ Id="organizations"; Label="AWS Organizations User Guide"; Docs="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html"; Search="AWS Organizations"; Tokens=@("organizations"); Regex=@("AWS Organizations","\bOrganizations\b") },
    @{ Id="scp"; Label="Search: Service Control Policies (SCP)"; Docs=$null; Search="Service Control Policies SCP AWS Organizations"; Tokens=@("scp"); Regex=@("\bSCP\b","Service Control Policy") },
    @{ Id="identity-center"; Label="IAM Identity Center User Guide"; Docs="https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html"; Search="IAM Identity Center"; Tokens=@("identity","center","identity-center"); Regex=@("Identity Center","AWS SSO") },

    @{ Id="kms"; Label="AWS KMS Developer Guide"; Docs="https://docs.aws.amazon.com/kms/latest/developerguide/overview.html"; Search="AWS KMS"; Tokens=@("kms"); Regex=@("\bKMS\b") },
    @{ Id="cloudtrail"; Label="AWS CloudTrail User Guide"; Docs="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html"; Search="AWS CloudTrail"; Tokens=@("cloudtrail"); Regex=@("CloudTrail") },
    @{ Id="cloudwatch"; Label="Amazon CloudWatch User Guide"; Docs="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html"; Search="Amazon CloudWatch"; Tokens=@("cloudwatch"); Regex=@("CloudWatch") },
    @{ Id="config"; Label="AWS Config Developer Guide"; Docs="https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html"; Search="AWS Config"; Tokens=@("config"); Regex=@("\bAWS Config\b") },

    @{ Id="vpc"; Label="Amazon VPC User Guide"; Docs="https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html"; Search="Amazon VPC"; Tokens=@("vpc"); Regex=@("\bVPC\b","Virtual Private Cloud") },
    @{ Id="vpc-endpoints"; Label="Search: VPC endpoints"; Docs=$null; Search="VPC endpoints"; Tokens=@("endpoints","endpoint"); Regex=@("VPC endpoint","Interface endpoint","Gateway endpoint") },
    @{ Id="privatelink"; Label="AWS PrivateLink User Guide"; Docs="https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html"; Search="AWS PrivateLink"; Tokens=@("privatelink"); Regex=@("PrivateLink") },
    @{ Id="sg-nacl"; Label="Search: security groups vs NACL"; Docs=$null; Search="security groups vs network ACLs VPC"; Tokens=@("sg","nacl"); Regex=@("Security Group","NACL","network ACL") },
    @{ Id="route53"; Label="Amazon Route 53 Developer Guide"; Docs="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html"; Search="Amazon Route 53 routing"; Tokens=@("route53"); Regex=@("Route 53","Route53") },

    @{ Id="s3"; Label="Amazon S3 User Guide"; Docs="https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html"; Search="Amazon S3"; Tokens=@("s3"); Regex=@("\bS3\b","Amazon S3") },
    @{ Id="s3-versioning"; Label="Search: S3 versioning"; Docs=$null; Search="S3 versioning"; Tokens=@("versioning"); Regex=@("versioning") },
    @{ Id="s3-replication"; Label="Search: S3 replication (CRR/SRR)"; Docs=$null; Search="S3 replication CRR SRR"; Tokens=@("replication"); Regex=@("CRR","SRR","replication") },
    @{ Id="s3-lifecycle"; Label="Search: S3 lifecycle rules"; Docs=$null; Search="S3 lifecycle rules"; Tokens=@("lifecycle"); Regex=@("Lifecycle") },
    @{ Id="s3-storage-classes"; Label="Search: S3 storage classes"; Docs=$null; Search="S3 storage classes"; Tokens=@("storage","classes"); Regex=@("storage class","Intelligent-Tiering","Glacier") },
    @{ Id="s3-sse-kms"; Label="Search: S3 SSE-KMS"; Docs=$null; Search="S3 SSE-KMS"; Tokens=@("sse","kms"); Regex=@("SSE-KMS") },

    @{ Id="ec2"; Label="Amazon EC2 User Guide"; Docs="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html"; Search="Amazon EC2"; Tokens=@("ec2"); Regex=@("\bEC2\b","Amazon EC2") },
    @{ Id="ebs"; Label="Search: Amazon EBS"; Docs=$null; Search="Amazon EBS"; Tokens=@("ebs"); Regex=@("\bEBS\b","Elastic Block Store") },
    @{ Id="efs"; Label="Amazon EFS User Guide"; Docs="https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html"; Search="Amazon EFS"; Tokens=@("efs"); Regex=@("\bEFS\b","Elastic File System") },
    @{ Id="autoscaling"; Label="EC2 Auto Scaling User Guide"; Docs="https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html"; Search="EC2 Auto Scaling"; Tokens=@("auto","scaling","autoscaling"); Regex=@("Auto Scaling","EC2 Auto Scaling") },
    @{ Id="purchase-options"; Label="Search: EC2 purchase options (RI/Savings Plans/Spot)"; Docs=$null; Search="EC2 purchase options Reserved Instances Savings Plans Spot"; Tokens=@("purchase","options"); Regex=@("Savings Plans","Reserved Instances","Spot") },

    @{ Id="elb"; Label="Elastic Load Balancing docs"; Docs="https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html"; Search="Elastic Load Balancing"; Tokens=@("alb","nlb","elb"); Regex=@("Load Balancer","ALB","NLB") },
    @{ Id="cloudfront"; Label="Amazon CloudFront Developer Guide"; Docs="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html"; Search="Amazon CloudFront"; Tokens=@("cloudfront"); Regex=@("CloudFront") },
    @{ Id="global-accelerator"; Label="AWS Global Accelerator Developer Guide"; Docs="https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html"; Search="AWS Global Accelerator"; Tokens=@("global","accelerator"); Regex=@("Global Accelerator") },

    @{ Id="dynamodb"; Label="Amazon DynamoDB Developer Guide"; Docs="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html"; Search="Amazon DynamoDB"; Tokens=@("dynamodb"); Regex=@("DynamoDB") },
    @{ Id="elasticache"; Label="Amazon ElastiCache User Guide"; Docs="https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html"; Search="Amazon ElastiCache"; Tokens=@("elasticache"); Regex=@("ElastiCache") },
    @{ Id="rds"; Label="Amazon RDS User Guide"; Docs="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html"; Search="Amazon RDS"; Tokens=@("rds"); Regex=@("\bRDS\b","Amazon RDS") },
    @{ Id="aurora"; Label="Search: Amazon Aurora"; Docs=$null; Search="Amazon Aurora"; Tokens=@("aurora"); Regex=@("Aurora") },

    @{ Id="cost-explorer"; Label="Search: AWS Cost Explorer"; Docs=$null; Search="AWS Cost Explorer"; Tokens=@("cost","explorer"); Regex=@("Cost Explorer") },
    @{ Id="budgets"; Label="Search: AWS Budgets"; Docs=$null; Search="AWS Budgets"; Tokens=@("budgets","budget"); Regex=@("Budgets","Budget") },
    @{ Id="cost-allocation-tags"; Label="Search: cost allocation tags"; Docs=$null; Search="cost allocation tags"; Tokens=@("allocation","tags"); Regex=@("cost allocation tags") },

    @{ Id="secretsmanager"; Label="AWS Secrets Manager User Guide"; Docs="https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html"; Search="AWS Secrets Manager"; Tokens=@("secrets"); Regex=@("Secrets Manager") },
    @{ Id="ssm-parameter-store"; Label="SSM Parameter Store (Systems Manager)"; Docs="https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html"; Search="SSM Parameter Store"; Tokens=@("parameter","store"); Regex=@("Parameter Store") },

    @{ Id="guardduty"; Label="Amazon GuardDuty User Guide"; Docs="https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html"; Search="Amazon GuardDuty"; Tokens=@(); Regex=@("GuardDuty") },
    @{ Id="inspector"; Label="Amazon Inspector User Guide"; Docs="https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html"; Search="Amazon Inspector"; Tokens=@(); Regex=@("Inspector") },
    @{ Id="securityhub"; Label="AWS Security Hub User Guide"; Docs="https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html"; Search="AWS Security Hub"; Tokens=@(); Regex=@("Security Hub") },
    @{ Id="macie"; Label="Amazon Macie User Guide"; Docs="https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html"; Search="Amazon Macie"; Tokens=@(); Regex=@("Macie") },
    @{ Id="detective"; Label="Amazon Detective User Guide"; Docs="https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html"; Search="Amazon Detective"; Tokens=@(); Regex=@("Detective") }
  )

  foreach ($d in $defs) {
    $matched = $false

    if ($d.ContainsKey("Tokens") -and $d.Tokens.Count -gt 0) {
      foreach ($t in $d.Tokens) {
        if ($tokens -contains $t.ToLowerInvariant()) { $matched = $true; break }
      }
    }

    if ($isBroadScan -and -not $matched -and $d.ContainsKey("Regex") -and $d.Regex.Count -gt 0) {
      foreach ($r in $d.Regex) {
        if ($content -match "(?i)$r") { $matched = $true; break }
      }
    }

    if (-not $matched) { continue }

    if (-not [string]::IsNullOrWhiteSpace($d.Docs)) {
      Add-UniqueLink -links $links -label $d.Label -url $d.Docs
      continue
    }

    $q = $d.Search
    if ([string]::IsNullOrWhiteSpace($q)) { $q = $d.Label }
    Add-UniqueLink -links $links -label $d.Label -url (New-AwsDocsSearchUrl -query $q)
  }

  if ($links.Count -eq 0) {
    $h1 = Get-FirstMarkdownH1 -content $content
    if (-not [string]::IsNullOrWhiteSpace($h1)) {
      Add-UniqueLink -links $links -label "Search in AWS docs: $h1" -url (New-AwsDocsSearchUrl -query $h1)
    } elseif (-not [string]::IsNullOrWhiteSpace($slug)) {
      Add-UniqueLink -links $links -label "Search in AWS docs: $slug" -url (New-AwsDocsSearchUrl -query $slug)
    }
  }

  if ($isBroadScan -and $links.Count -gt 12) {
    return $links.GetRange(0, 12).ToArray()
  }

  return $links.ToArray()
}

function Build-ReferencesBlock([string]$fromDir, [string]$awsSaaRoot, [string]$filePath, [string]$content) {
  $referencesReadme = Join-Path $awsSaaRoot "references/README.md"
  $examGuide = Join-Path $awsSaaRoot "references/exam-guide.md"
  $glossary = Join-Path $awsSaaRoot "references/glossary.md"
  $awsServices = Join-Path $awsSaaRoot "references/aws-services.md"
  $examKeypoints = Join-Path $awsSaaRoot "exam-keypoints.md"
  $examTrapBank = Join-Path $awsSaaRoot "exam-trap-bank.md"

  $refRel = Get-RelativePath -fromDir $fromDir -toPath $referencesReadme
  $examRel = Get-RelativePath -fromDir $fromDir -toPath $examGuide
  $glossRel = Get-RelativePath -fromDir $fromDir -toPath $glossary
  $svcRel = Get-RelativePath -fromDir $fromDir -toPath $awsServices
  $keyRel = Get-RelativePath -fromDir $fromDir -toPath $examKeypoints
  $trapRel = Get-RelativePath -fromDir $fromDir -toPath $examTrapBank

  $official = @(Get-OfficialAwsDocsLinks -filePath $filePath -content $content)
  $officialLines = @()
  if ($official.Count -gt 0) {
    $officialLines += "- Official AWS documentation:"
    foreach ($x in $official) {
      $officialLines += "  - $(New-MarkdownLink -label $x.Label -urlOrPath $x.Url)"
    }
  }

  $lines = @(
    "## References",
    "",
    "- Internal references:",
    "  - $(New-MarkdownLink -label 'References index' -urlOrPath $refRel)",
    "  - $(New-MarkdownLink -label 'Exam guide (SAA-C03)' -urlOrPath $examRel)",
    "  - $(New-MarkdownLink -label 'Glossary' -urlOrPath $glossRel)",
    "  - $(New-MarkdownLink -label 'AWS services list' -urlOrPath $svcRel)",
    "  - $(New-MarkdownLink -label 'Exam keypoints' -urlOrPath $keyRel)",
    "  - $(New-MarkdownLink -label 'Exam trap bank' -urlOrPath $trapRel)",
    ""
  ) + $officialLines

  return ($lines -join "`n")
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$awsSaaRoot = Join-Path $repoRoot "aws-saa"

if (-not (Test-Path $awsSaaRoot)) {
  throw "aws-saa root not found at: $awsSaaRoot"
}

$targets = @(Get-ChildItem -Recurse -File -Path $awsSaaRoot |
  Where-Object { $_.Extension -eq ".md" } |
  Where-Object {
    $_.FullName -like "*\week??\day??\??-*.md" -or
    ($_.FullName -like "*\special-lectures\*.md" -and $_.Name -ne "README.md")
  } |
  Where-Object { $_.Name -notmatch "(?i)quiz" })

$changed = 0
foreach ($file in $targets) {
  $path = $file.FullName
  $content = Read-TextFileUtf8NoBom $path
  $nl = Get-NewLine $content
  $lines = $content -split "\r?\n", -1

  $kept = New-Object System.Collections.Generic.List[string]
  for ($i = 0; $i -lt $lines.Length; $i++) {
    $line = $lines[$i]

    if ($line -match "^(?i)##\s*References\s*$") {
      $i++
      while ($i -lt $lines.Length -and ($lines[$i] -notmatch "^##\s+")) {
        $i++
      }
      $i--
      continue
    }

    $kept.Add($line)
  }

  while ($kept.Count -gt 0 -and $kept[$kept.Count - 1] -eq "") {
    $kept.RemoveAt($kept.Count - 1)
  }

  $blockText = (Build-ReferencesBlock -fromDir $file.DirectoryName -awsSaaRoot $awsSaaRoot -filePath $path -content $content).TrimEnd()
  $blockLines = $blockText -split "\r?\n"

  $insertIndex = $kept.Count
  for ($i = 0; $i -lt $kept.Count; $i++) {
    if ($kept[$i] -match "^##\s*Back\s*$") { $insertIndex = $i; break }
    if ($kept[$i] -match "^-\\s*Back\\s*:") { $insertIndex = $i; break }
  }

  if ($insertIndex -gt 0 -and $kept[$insertIndex - 1] -ne "") {
    $kept.Insert($insertIndex, "")
    $insertIndex++
  }

  foreach ($bl in $blockLines) {
    $kept.Insert($insertIndex, $bl)
    $insertIndex++
  }

  $kept.Insert($insertIndex, "")

  $newContent = ($kept.ToArray() -join $nl).TrimEnd() + $nl

  if ($WhatIf) {
    Write-Host "[WhatIf] would update: $($file.FullName)"
    continue
  }

  Write-TextFileUtf8NoBom $path $newContent
  $changed++
}

Write-Host "Updated files: $changed / $($targets.Count)"
