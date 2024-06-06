import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            global log_message
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                return result
            except Exception as e:
                error_type = type(e).__name__
                log_message = (f"{func.__name__} error: {error_type}. "
                               f"Inputs: {args}, {kwargs}")
                raise
            finally:
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)

        return wrapper

    return decorator
