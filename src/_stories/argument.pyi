from typing import Callable
from typing import List
from typing import Tuple

def arguments(*names: Tuple[str]) -> Callable: ...
def get_arguments(f: Callable) -> List[str]: ...