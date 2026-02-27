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

