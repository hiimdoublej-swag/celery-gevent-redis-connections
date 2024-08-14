Update 2023-04-11:
The problem seems to go away by setting `result_backend_thread_safe` to `True`.
The connections stayed at 24.

The repository contains a reproducible case of the celery/redis/gevent connection leak bug [as described here](https://github.com/celery/celery/issues/6819)

Steps to reproduce:

1. Start the containers
`docker compose up worker runner redis`
2. On a separate shell, observe the connection count using the following command.
`watch -n 1 "docker compose exec redis redis-cli info | grep -i connected_clients"`
3. Let it run for a few seconds and the number reported by the previous step should grow steadily. In my case it reached 300 after 30 seconds.
