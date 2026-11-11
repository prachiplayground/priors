# Schema

priors stores two linked record types. A **source record** describes an article, paper, talk or podcast. A **decision record** describes one distinct product decision found in a source. One source can yield several decisions.

Machine-readable versions: [`schema/source_record.schema.json`](../schema/source_record.schema.json), [`schema/decision_record.schema.json`](../schema/decision_record.schema.json).

## Rules

- A field is `null` when the source doesn't state it. Never fill a field by inference.
- `results` contains only lifts the source itself reports.
- Every extracted field on a decision record has an evidence pointer (section or paragraph of the source), never copied text.
- `ethics_considerations` is assessed for every decision, whatever its bucket. A `null` is data: it records that the source never raised one.

## Category buckets

Each decision has one primary bucket and up to two secondary buckets.

| Bucket | Covers |
| --- | --- |
| `personalization` | Feeds, homepages, "for you" surfaces, user modeling |
| `search_discovery` | Query understanding, search ranking, browse and navigation |
| `pricing_monetization` | Dynamic pricing, plans and tiers, discounts, paywalls |
| `ads` | Ad ranking, auctions, advertiser tools, ad load |
| `marketplace` | Matching, supply/demand balance, liquidity, two-sided incentives |
| `growth` | Funnels, referrals, viral loops, SEO, onboarding conversion |
| `engagement_retention` | Notifications, habit loops, churn reduction, lifecycle |
| `experimentation` | A/B platforms, metric design, guardrails, causal inference |
| `trust_safety` | Protecting users from bad actors: fraud, spam, moderation, review quality |
| `responsible_ai` | Effects of the company's own systems: fairness, privacy, transparency, user controls, wellbeing, compliance, governance |
| `ux_design` | Interface changes, information architecture, accessibility |
| `ai_llm_features` | Assistants, generative features, evals, agentic workflows |
| `platform_infra` | Build vs. buy, migrations, platform consolidation, tech debt |

## Source record

| Field | Type | Notes |
| --- | --- | --- |
| `source_id` | string | e.g. `airbnb-2018-listing-embeddings` |
| `title`, `url` | string | |
| `source_type` | enum | `blog`, `paper`, `talk`, `podcast`, `book` |
| `company` | string | Company the source is about |
| `year` | int | |
| `authors` | list | |
| `source_perspective` | enum | `company_self_report`, `independent` |
| `status` | enum | `found`, `fetched`, `extracted`, `reviewed`, `published` |

## Decision record: core fields

| Group | Field | Type |
| --- | --- | --- |
| Identity | `decision_id`, `source_id` | string |
| Classification | `primary_category`, `secondary_categories` | enum, list (max 2) |
| Context | `surface` | enum: feed, search, homepage, notifications, checkout, pricing_page, internal_tool, other |
| Context | `business_model`, `sidedness` | enum; `one_sided` or `two_sided` |
| Matching context | `company_stage`, `company_scale`, `industry`, `region`, `user_segment`, `constraints` | strings / lists |
| PM story | `problem`, `key_decision` | 1–2 sentences each |
| PM story | `objective_metric`, `guardrail_metrics` | string, list |
| PM story | `approach`, `techniques` | summary, tag list |
| PRD-shaped | `assumptions`, `risks`, `dependencies`, `rollout_strategy` | lists / text |
| Results | `results[]` | {metric, change, unit, method} |
| Lessons | `what_failed`, `lessons` | text or null |
| Ethics | `ethics_considerations` | list of {concern_type, note} or null |
| Lineage | `builds_on`, `superseded_by` | list of decision ids |
| Quality | `evidence`, `confidence`, `review_status` | map, 0–1, enum |

## Decision record: category-specific fields

Filled only for the decision's primary bucket. Stored under `category_fields`.

| Bucket | Fields |
| --- | --- |
| `personalization` | `pipeline_stage`, `signal_freshness`, `cold_start_strategy`, `user_representation` |
| `search_discovery` | `query_type`, `ranking_signals`, `personalized` |
| `pricing_monetization` | `pricing_mechanism`, `price_unit`, `elasticity_tested`, `fairness_or_trust_constraint` |
| `ads` | `auction_type`, `ad_load_tradeoff`, `advertiser_vs_user_metric` |
| `marketplace` | `side_targeted`, `liquidity_metric`, `matching_mechanism`, `incentive_type` |
| `growth` | `funnel_stage`, `channel`, `loop_type` |
| `engagement_retention` | `retention_horizon`, `engagement_vs_wellbeing_tradeoff`, `lifecycle_stage` |
| `experimentation` | `method`, `variance_reduction`, `metric_problem_solved` |
| `trust_safety` | `harm_type`, `precision_recall_tradeoff`, `human_in_loop` |
| `responsible_ai` | `concern_type`, `affected_group`, `mitigation`, `regulatory_driver`, `governance_mechanism`, `business_tradeoff` |
| `ux_design` | `change_type`, `research_method` |
| `ai_llm_features` | `model_role`, `offline_vs_online`, `eval_approach`, `guardrails` |
| `platform_infra` | `decision_type`, `driver`, `migration_strategy`, `reported_outcome` |
