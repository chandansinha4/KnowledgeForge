# Transcript Processing Threshold Experiment

## 1. Objective

Determine when KnowledgeForge should process a YouTube transcript
directly with the LLM and when it should switch to a chunked
processing strategy.

The goal is to establish an evidence-based threshold rather than
choosing an arbitrary transcript size.

---

## 2. Problem

KnowledgeForge currently sends the complete YouTube transcript
to the Knowledge Agent.

This works well for the MIT 18.06 Lecture 1 transcript using
Gemini 3.5 Flash.

However, longer educational videos may introduce:

- Higher input token usage
- Higher output token usage
- Increased latency
- Larger context requirements
- Greater risk of incomplete or lower-quality output

Chunking can help manage large transcripts, but it also introduces
additional LLM calls and processing complexity.

Therefore, chunking should only be introduced when the benefits
justify the additional complexity.

---

## 3. Hypothesis

Direct transcript processing should remain the default for
short and medium-sized transcripts.

As transcript size increases, there may be a point where direct
processing results in unacceptable latency, token usage, or
quality degradation.

Beyond this point, a chunked processing strategy may provide
better reliability and context management.

---

## 4. Current Baseline

### Model

- Provider: Gemini
- Model: gemini-3.5-flash

### Knowledge Prompt

Current optimized KnowledgeForge knowledge extraction prompt.

### Baseline Transcript

MIT 18.06 Linear Algebra — Lecture 1

### Baseline Measurements

| Metric | Result |
|---|---:|
| Input tokens | 6,938 |
| Output tokens | 3,996 |
| Total tokens | 10,934 |
| Quality | Good |

These measurements represent the current direct-processing
baseline.

### Prompt Version

Knowledge Prompt V3 — concise source-grounded knowledge extraction

### Model Configuration

- Provider: Gemini
- Model: gemini-3.5-flash
- Prompt: Knowledge Prompt V3

---

## 5. Experimental Variables

### Transcript

- Character count
- Word count
- Estimated token count
- Actual LLM input tokens

### Generation

- Provider
- Model
- Prompt version
- Output tokens
- Total tokens
- Latency

### Quality

- Information coverage
- Factual consistency
- Completeness
- Structure
- Task adherence

### Video

- Duration
- Words
- Words per minute
- Character count
- Estimated token count

---

## 6. Experimental Method

Test transcripts with different sizes using the same:

- Provider
- Model
- Knowledge prompt
- Generation configuration
- Processing pipeline

Initially, direct processing will be tested across multiple
transcript sizes.

Example test ranges:

| Test | Approximate Transcript Size | Strategy |
|---|---:|---|
| T1 | ~3K tokens | Direct |
| T2 | ~7K tokens | Direct |
| T3 | ~12K tokens | Direct |
| T4 | ~20K tokens | Direct |
| T5 | ~30K tokens | Direct |

The actual transcript sizes will be measured rather than assumed.

---

## 7. Results

_To be populated as experiments are performed._

| Test | Duration | Words | WPM | Estimated Tokens | Actual Input Tokens | Output Tokens | Total Tokens | Latency | Quality |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| T1 - MIT Lecture 1 | 39:48 | 4,964 | ~125 | 6,453 | 6,938 | 3,996 | 10,934 | ~16s | Incomplete |
| T2 | 1:07:33 | 10,498 | ~155 | 13,647 | 14,041 | 3,996 | 18,037 | ~29s | Incomplete |
| T3 | 1:25:36 | 13,470 | ~157 | 17,511 | TBD | TBD | TBD | TBD | TBD |
| T4 | TBD | 19,445 | TBD | 25,278 | TBD | TBD | TBD | TBD | TBD |

### T1 Observation

The direct-generation request completed successfully, but the
generated KnowledgeDocument was incomplete. The response ended
mid-section rather than reaching a natural conclusion.

The model generated 3,996 output tokens, which is close to the
configured maximum output-token limit. This suggests that the
response may have been truncated by the output budget rather
than by an input/context limitation.

This needs to be investigated in subsequent experiments.

### T2 Observation

T2 reproduced the output truncation observed in T1.
The model generated exactly 3,996 output tokens despite
having a substantially larger input.

This strengthens the hypothesis that the current output-token
limit is responsible for the incomplete KnowledgeDocuments.

Latency increased from approximately 16 seconds in T1 to
approximately 29 seconds in T2.
### Observation

The word-based token estimator predicted 6,453 tokens,
while Gemini reported 6,938 actual input tokens.

The estimator therefore underestimated the actual input
by approximately 7.5%.

The estimate is considered suitable as a rough routing signal,
but actual provider-reported usage remains authoritative.
---

## 8. Findings

_To be populated after sufficient experiments have been completed._

### Preliminary Finding

The first experiment revealed an output-length limitation at
approximately 6.5K estimated transcript tokens.

However, this is not sufficient evidence to establish the
chunking threshold. Further experiments are required to
determine whether the issue is caused by transcript size,
output-token limits, or both.

### Finding — Coverage Prompt

At approximately 50K input tokens, the original Knowledge
prompt produced a 3,513-token document with noticeable
omission of later sections.

A controlled rerun using the same transcript, model,
generation configuration, and 8,192-token output limit,
but with explicit full-source coverage instructions,
produced 5,970 output tokens and substantially improved
coverage of later sections.

This indicates that incomplete coverage at this input size
was not solely caused by the model's output-token limit.
Prompt instructions materially influenced how the available
output budget was allocated across the source.
---

## 9. Threshold Decision

_To be determined from experimental results._

The threshold should consider:

1. Output quality
2. Completeness
3. Latency
4. Token usage
5. Reliability

The threshold should not be based solely on token count.

---

## 10. Proposed Routing Strategy

After the threshold is established, KnowledgeForge may use:

```text
Transcript
    |
    +-- Below threshold --> Direct processing
    |
    +-- Above threshold --> Chunked processing