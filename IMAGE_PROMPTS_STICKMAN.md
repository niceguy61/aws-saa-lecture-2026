# 스틱맨 고객사례 삽화 프롬프트 모음 (캐주얼/IT Office)

목표: 각 서비스별 `## 고객 사례 (스토리)` 바로 아래에 넣을 **캐주얼한 스틱맨 일러스트**를 일관된 톤으로 생성한다.

## 공통 스타일(고정)

아래 블록을 **매번 프롬프트 맨 앞에 그대로** 붙인다.

```text
Casual flat vector illustration, cute stickman characters with consistent simple design (round heads, thin limbs), friendly vibe, modern IT office background (desks, laptops, monitors, whiteboard), soft pastel colors, clean outlines, minimal shading, slightly playful composition, high clarity, 16:9, 2–4 stickmen in the scene, small symbolic icons allowed (lock, key, shield, clock, server, folder), no brand logos, no readable text, no UI screenshots, no watermark.
```

## 생성 팁(권장)

- 이미지 안 텍스트는 깨질 수 있으니 **글자/로고는 넣지 않는다**(화이트보드도 “박스/화살표”만).
- 시리즈 느낌을 위해 **same style / consistent character design**을 유지한다.

---

## Week01 / Day01 (Access control)

### `aws-saa/week01/day01/01-iam.md`

```text
Scene: In a cozy IT office, three stickmen collaborate. A developer looks mildly stressed holding a laptop, while a security teammate calmly points at a whiteboard showing a messy permission grid made of simple boxes and arrows (no text). Another teammate holds a clean “policy template” sheet. The security teammate places a small lock icon over a simplified “least privilege” area, turning messy sticky notes into a neat template vibe. Casual, relatable teamwork mood.
```

### `aws-saa/week01/day01/02-sts.md`

```text
Scene: In an IT office, three stickmen. One stickman is about to hand over a big keychain (long-term keys) and looks worried; another stickman stops them and instead hands a small temporary badge with a timer icon (OTP vibe). A third stickman points to a role “borrow” concept shown as a simple ID card moving between two desk areas (no text). Emphasize “temporary access is safer than sharing keys”, friendly and casual.
```

### `aws-saa/week01/day01/03-organizations-scp.md`

```text
Scene: IT office meeting with three stickmen in front of a whiteboard showing an organization tree diagram (root → OUs → multiple account boxes, no text). A clear guardrail/barrier icon sits across the tree labeled only by symbols (shield/stop icon). Teams inside account boxes move fast with small gear icons, but the guardrail prevents risky actions. The vibe is “governance guardrails without slowing teams”, casual and clean.
```

### `aws-saa/week01/day01/04-identity-center.md`

```text
Scene: Modern IT office with a single “SSO doorway” metaphor: two stickmen walk through one secure door with an ID card icon, then choose between multiple account rooms shown as simple door icons (no text). A third stickman admin at a central desk assigns access using a checklist board made of plain checkboxes (no text). Friendly, casual onboarding/offboarding vibe.
```

---

## Week01 / Day02 (Data protection)

### `aws-saa/week01/day02/01-kms.md`

```text
Scene: IT office with three stickmen around a “key vault” safe icon. A developer tries to open an encrypted data box but is blocked by a gate icon (policy gate). A security teammate points at a clipboard showing a simple checklist with icons (no text). A third stickman indicates that even if the developer has permission, the key vault gate (key policy) is the final checkpoint. Clean, casual “policy gate” message.
```

### `aws-saa/week01/day02/02-secrets-vs-parameter-store.md`

```text
Scene: Desk in an IT office with two storage metaphors side-by-side: a small secure vault box (secrets) and a labeled drawer organizer (parameters) shown with icons only (no text). A rotation circular-arrows icon appears near the vault box only. Three stickmen discuss and choose the vault for rotation needs, casual and friendly.
```

### `aws-saa/week01/day02/03-s3-sse-kms.md`

```text
Scene: IT office flow diagram as a playful illustration: a stickman requests a file from a storage box icon; the storage box then calls a key vault icon to decrypt (on behalf) before handing the file back. Show a small “blocked” sign at the key vault gate to imply AccessDenied. Two other stickmen point to the vault gate as the hidden bottleneck. No text, use icons and arrows only.
```

---

## Week01 / Day03 (Audit / compliance / detection)

### `aws-saa/week01/day03/01-cloudtrail.md`

```text
Scene: Incident response in an IT office. Three stickmen: one detective-style (simple magnifying glass icon) reviews a timeline on a monitor made of icons (API call dots, user icon, clock icon; no text). Another stickman points to an archive shelf icon for long-term logs. The third looks relieved as the “who did it” evidence is found. Friendly but serious enough for audit.
```

### `aws-saa/week01/day03/02-config.md`

```text
Scene: Compliance review in an IT office. Three stickmen: an auditor asks questions (question mark icon), an engineer points to a big compliance board showing green/red status dots for resources and a small history timeline strip (icons only, no text). Another teammate holds a “rule” card icon. The vibe is “state/compliance view”, calm and organized.
```

### `aws-saa/week01/day03/03-detection-services.md`

```text
Scene: Security monitoring in an IT office. Three stickmen: one watches a radar icon producing alert dots; findings flow via arrows into a central hub board icon. Another stickman receives an alert notification bubble icon. A third points out layers: sources → detection → aggregation, shown only with icons (no text). Casual, readable.
```

---

## Week01 / Day04 (Network boundaries)

### `aws-saa/week01/day04/01-sg-vs-nacl.md`

```text
Scene: Two-layer “door security” metaphor inside an IT office. Show a building entrance gate icon (subnet-level) and a specific room door icon (instance-level). Three stickmen compare them: the room door has an automatic return-arrow icon (stateful), while the entrance gate requires a separate return-arrow icon (stateless). Clean, playful but accurate.
```

### `aws-saa/week01/day04/02-vpc-endpoints-privatelink.md`

```text
Scene: Network path metaphor in an IT office. A private tunnel connects a desk area to a cloud service icon (safe route). Next to it, a public road goes through a toll booth icon (NAT cost) toward the same cloud icon. Three stickmen choose the private tunnel when “no internet” and “cost saving” vibes apply. No text, use icons (shield, coin, tunnel).
```

---

## Week01 / Day05 (Special Lecture + Week Summary)

### `aws-saa/week01/day05/01-theory.md`

```text
Scene: Week summary review in an IT office. Four stickmen around a big whiteboard “battle map” of secure architecture patterns made only of icons and arrows (no text). Show grouped icon clusters: access control (lock + ID card), data protection (key vault + secret box), audit/compliance (timeline + checklist), private connectivity (tunnel + shield). One stickman points at a “trap” area with a red warning triangle icon, another marks “best choice” with a green check icon. Casual, debrief vibe like a friendly retro meeting.
```

---

## Week02 / Day01 (Resilience basics)

### `aws-saa/week02/day01/01-route53-routing.md`

```text
Scene: Traffic director in an IT office. A signpost routes user icons to two data-center buildings; one building has a heartbeat/health icon. Show automatic switch to the healthy building with arrows. Also include a percentage dial icon to hint weighted routing. Three stickmen coordinate calmly, casual and readable.
```

### `aws-saa/week02/day01/02-dr-strategies.md`

```text
Scene: IT office whiteboard “DR menu” with four option cards represented only by icons: archive box (backup/restore), small running core (pilot light), smaller full stack (warm standby), two full stacks (active/active). A clock icon and database icon guide the choice (RPO/RTO concept). Three stickmen discuss tradeoffs with a playful but clear vibe.
```

---

## Week02 / Day02 (Self-healing)

### `aws-saa/week02/day02/01-alb-vs-nlb.md`

```text
Scene: IT office desk with two load balancer devices: one shows HTTP routing cues (path/host icons, small layer-7 symbol), the other shows raw throughput/protocol cues (speedometer icon, layer-4 symbol). Three stickmen point at requirement icons to pick the right one. No text, clean and casual.
```

### `aws-saa/week02/day02/02-auto-scaling.md`

```text
Scene: Thermostat metaphor in an IT office. A stickman sets a desired level on a simple dial icon; server icons automatically scale up/down. Show one server failing a health check (small cross icon) and being replaced by a fresh server icon. Two other stickmen watch and smile as it self-heals. No text.
```

---

## Week02 / Day03 (Storage resilience)

### `aws-saa/week02/day03/01-s3-versioning.md`

```text
Scene: Version stack in an IT office. A document/file icon has multiple versions stacked with small timestamp dots (no text). A delete marker icon appears, but an older version is restored with a rewind icon. Three stickmen look relieved. Clean and casual.
```

### `aws-saa/week02/day03/02-s3-replication.md`

```text
Scene: Two storage bucket icons in two distant locations connected by an arrow. A version stack icon is shown on both sides to imply versioning prerequisite. A compliance stamp icon hints regulation/DR. Three stickmen check the prerequisites and approve. No text, readable.
```

### `aws-saa/week02/day03/03-ebs-snapshot.md`

```text
Scene: Disk snapshot in an IT office. A camera icon takes a snapshot of a disk/volume icon; later the snapshot restores a new disk attached to a server icon. Add a calendar/schedule icon to suggest periodic snapshots. Three stickmen coordinate a calm recovery. No text.
```

---

## Week02 / Day04 (Database resilience)

### `aws-saa/week02/day04/01-rds-aurora-multi-az-vs-rr.md`

```text
Scene: Database topology in an IT office. One primary database icon has a standby sibling (HA failover arrow), and separate read replicas branch out (read scaling arrows). Three stickmen point to different requirement icons: uptime shield vs read speed gauge. Clean, casual, no text.
```

### `aws-saa/week02/day04/02-dynamodb-resilience.md`

```text
Scene: Timeline rollback in an IT office. A NoSQL table icon has a time slider/rewind control; after an accidental update (oops icon), the table returns to an earlier point (rewind). Three stickmen celebrate the rollback. No text, friendly and clear.
```

---

## Week02 / Day05 (Special Lecture + Week Summary)

### `aws-saa/week02/day05/01-theory.md`

```text
Scene: Resilience patterns recap in an IT office. Four stickmen run a “system resilience rehearsal” on a whiteboard made of icons only (no text): traffic routing (signpost + heartbeat), self-healing (thermostat + replace icon), decoupling (queue box buffering a spike wave), and DR strategy menu (archive vs dual-site icons). One stickman places a small clock + database icon to represent RPO/RTO, while another highlights retry/DLQ with a loop arrow and a dead-letter box icon. Friendly, energetic summary vibe.
```

---

## Week03 / Day01 (Performance thinking + compute)

### `aws-saa/week03/day01/00-theory-index.md`

```text
Scene: A friendly IT office “performance triage” moment. Three stickmen stand around a whiteboard showing four simple bottleneck buckets (CPU chip icon, memory chip icon, network cable icon, disk icon) with arrows from a “slow app” box (no text). One stickman holds a small stopwatch icon labeled only by symbols (p95/p99 vibe as two stacked percentile dots, no text). Another stickman places a magnifying glass over the CPU bucket to show “diagnosis first”. Calm, methodical vibe.
```

### `aws-saa/week03/day01/01-ec2.md`

```text
Scene: In an IT office, three stickmen debate EC2 choices. One stickman points at a whiteboard decision tree made of icons: CPU-heavy -> “C” badge icon, memory-heavy -> “R/X” badge icon, bursty -> “T” badge icon (use simple letter badges as abstract icons, no readable words). Another stickman holds a tiny hourglass + coin icon to imply cost/perf tradeoff. In the corner, a “credit meter” icon drains to empty with a red warning triangle to hint burst credits. Friendly, casual, but clear.
```

### `aws-saa/week03/day01/02-cloudwatch.md`

```text
Scene: IT office monitoring station. Three stickmen look at a monitor showing three simple charts (no text): CPU line, disk queue spikes (stacked dots), and a “credit bar” dropping. One stickman points to a checklist board with four icons (CPU, disk, network, credit) to imply cross-checking metrics. Another stickman holds a magnifying glass and a small “aha” lightbulb icon. Clean, minimal, no UI screenshot style.
```

---

## Week03 / Day02 (Edge caching + network acceleration)

### `aws-saa/week03/day02/00-theory-index.md`

```text
Scene: IT office whiteboard showing two lanes to “global users” (globe icon). Lane A: CloudFront cache layer (stacked boxes with a snowflake/cache icon) close to users; Lane B: Global Accelerator path (globe -> anycast entry pin -> fast backbone line to endpoint). Three stickmen compare the two with a split-screen vibe: one stickman places a cache icon on the left, another places a routing/path icon on the right. No text, icons and arrows only.
```

### `aws-saa/week03/day02/01-cloudfront.md`

```text
Scene: A playful cache-hit/cache-miss illustration in an IT office. Users (small person icons) request a file; the request hits a nearby “edge cache” box (smiley check icon) most of the time, and sometimes goes to an “origin” storage box (longer arrow). Include a small TTL hourglass icon above the cache, and a “broom/erase” icon for invalidation (no text). Three stickmen adjust a simple dial icon (TTL) and smile as the origin load decreases (down arrow).
```

### `aws-saa/week03/day02/02-global-accelerator.md`

```text
Scene: Global network path optimization in an IT office. A globe icon with multiple entry pins (anycast vibe) routes traffic to the nearest pin, then a thick “fast backbone” line goes to a server endpoint icon. Add a “fixed IP badge” icon (simple ID card with numbers as abstract dots, no readable text) to hint static IP. Three stickmen: one draws the shortest route, another checks a health icon on endpoints, another holds a shield icon for reliability. No text.
```

---

## Week03 / Day03 (Storage performance: EBS/EFS)

### `aws-saa/week03/day03/00-theory-index.md`

```text
Scene: IT office “storage choice” board. Left side: EBS block disk icon with two sliders (IOPS and throughput) and a speedometer. Right side: EFS shared folder icon connected to three server icons (shared lines). A stickman tries to connect two servers to one disk and gets a red “not shareable” symbol, while another stickman happily connects multiple servers to the shared folder with green checks. No text, clear contrast.
```

### `aws-saa/week03/day03/01-ebs.md`

```text
Scene: EBS tuning moment in an IT office. A disk icon sits next to a queue icon (stack of waiting dots) that is overflowing; a stickman turns two knobs labeled only by icons (IOPS lightning bolt, throughput water-flow icon). Another stickman watches a chart stabilize (line becomes smooth). Include a small “gp3” and “io2” abstract tag as simple colored chips (no readable words) to imply volume type choices. Casual, clean.
```

### `aws-saa/week03/day03/02-efs.md`

```text
Scene: Shared uploads problem in an IT office. Three web-server icons each have a small folder; the folders look inconsistent (warning icons). A stickman replaces them with one central shared folder icon (EFS) connected to all servers with neat lines. Another stickman tears up a “sync script” paper (no text) to show reduced ops pain. Friendly, relief vibe.
```

---

## Week03 / Day04 (DB performance + caching)

### `aws-saa/week03/day04/00-theory-index.md`

```text
Scene: IT office “DB performance ladder” board. Three steps shown as icons only: step 1 cache (cache box), step 2 access pattern/index (key + index grid), step 3 read scaling (one DB branching into multiple read nodes). Three stickmen walk up the steps, each carrying an icon: stopwatch (latency), coin (cost), and shield (reliability). No text, crisp and instructive.
```

### `aws-saa/week03/day04/01-dynamodb.md`

```text
Scene: DynamoDB access pattern illustration in an IT office. A table is shown as partition boxes; one partition is “hot” with a small flame icon and many arrows hitting it. Another stickman redraws the key design as evenly distributed partitions with balanced arrows. Show Query as a magnifying glass targeting one partition box, and Scan as a sweeping broom passing across all boxes with a red warning triangle (no text). Clear, casual.
```

### `aws-saa/week03/day04/02-elasticache.md`

```text
Scene: Read-heavy hot path in an IT office. App icon requests data; most requests go to a cache box first (green check), and only misses go to a DB icon (longer arrow). Add a small “freshness” icon (tiny clock) near the cache to hint invalidation/consistency tradeoff. Three stickmen: one points at reduced DB load (down arrow), another points at a warning icon near the clock, and the third holds a balancing scale icon to show tradeoff. No text.
```

### `aws-saa/week03/day04/03-aurora.md`

```text
Scene: Read scaling concept in an IT office. One primary DB icon handles writes (pen icon), and multiple read replica DB icons branch out (eye icon) with arrows to many user icons. A stickman routes read traffic to the read cluster, while another stickman points at an index icon (grid) and a connection pool icon (simple chain links) to show tuning hints. Casual and clear, no text.
```

---

## Week03 / Day05 (Special Lecture + Week Summary)

### `aws-saa/week03/day05/01-theory.md`

```text
Scene: Week 3 recap in an IT office. Four stickmen around a big whiteboard “diagnosis order” flow drawn with icons only: cache (cache box) -> DB pattern (key + index grid) -> storage I/O (disk + speedometer) -> compute (CPU chip) -> network path (globe + route line). One stickman marks “trap” with a red warning triangle near “Scan” and “wrong accelerator choice” icons, another marks “best move” with a green check near cache-first. Friendly debrief vibe, no text.
```
