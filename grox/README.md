# Grox: Content Understanding Service

Grox is the content understanding component of the X algorithm system. It uses transformer models and classifiers to analyze incoming content (posts, media, user interactions) and extract features used by the ranking pipeline.

## Architecture

Grox processes content through several stages:

- **Engine** (`engine.py`): Async task execution engine with worker processes
- **Dispatcher** (`dispatcher.py`): Routes tasks to appropriate handlers
- **Classifiers** (`classifiers/`): Content classification models (sentiment, topic, engagement prediction)
- **Data Loaders** (`data_loaders/`): Kafka, Strato, and MQ connectors for input streams
- **Embedder** (`embedder/`): Multimodal embedding models (v2, v5)
- **Generators** (`generators/`): Stream and task generators
- **Plans** (`plans/`): Plan execution and state management
- **Schedules** (`schedules/`): Task scheduling and worker management
- **Summarizer** (`summarizer/`): Content summarization for context
- **Tasks** (`tasks/`): Individual task handlers

## Utilities

The `lib/` directory contains reusable utilities:

- `utils.py`: String case conversion (`camel_to_snake`, `snake_to_camel`)
- `stream.py`: Async stream utilities (`parallel_merge`)

## Testing

Grox uses `pytest` with `pytest-asyncio` for async tests.

```bash
# Run all grox tests (requires grox dependencies)
pytest grox/tests/ -v

# Run specific test file
pytest grox/tests/test_utils.py -v

# Run with uv (if grox has pyproject.toml)
uv run pytest grox/tests/ -v
```

## Development

Grox uses a multiprocessing async architecture. Key patterns:

- `Engine` manages worker processes and task queues
- `parallel_merge` combines multiple async streams
- Classifiers and embedders are loaded lazily

For more detail on the Grox component, see the main X Algorithm README and architecture diagrams.
