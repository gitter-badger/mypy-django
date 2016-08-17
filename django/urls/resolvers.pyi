# Stubs for django.urls.resolvers (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Callable, Dict, Iterable, List, Optional, Pattern, Tuple, Union

from django.http.response import HttpResponse
from django.utils.datastructures import MultiValueDict

# Auxiliar types
URLPattern = Union['RegexURLResolver', 'RegexURLPattern']
Params = Dict[str, object]  # Arguments for views
# Auxiliar type for allowed resolver configurations
URLConf = Union[str, List[URLPattern]]

# The result type for regex_helper.normalize()
NormalizedRegexForms = List[Tuple[str, List[str]]]
ReverseLookup = MultiValueDict[str, Tuple[NormalizedRegexForms, str, Params]]
Namespace = Dict[str, Tuple[str, 'RegexURLResolver']]
AppDict = Dict[str, List[str]]

class ResolverMatch:
    func = ...  # type: Callable
    args = ...  # type: Iterable[object]
    kwargs = ...  # type: Params
    url_name = ...  # type: Optional[str]
    app_names = ...  # type: List[str]
    app_name = ...  # type: str
    namespaces = ...  # type: List[str]
    namespace = ...  # type: str
    view_name = ...  # type: str
    def __init__(self, func: Callable, args: Iterable[object], kwargs: Params, url_name: str=None, app_names: Iterable[str]=None, namespaces: Iterable[str]=None) -> None: ...
    def __getitem__(self, index: int) -> Any: ...

def get_resolver(urlconf: Optional[URLConf]=None) -> 'RegexURLResolver': ...
def get_ns_resolver(ns_pattern: str, resolver: 'RegexURLResolver') -> 'RegexURLResolver': ...

class LocaleRegexProvider:
    def __init__(self, regex: Optional[str]) -> None: ...
    @property
    def regex(self) -> Pattern[str]: ...

class RegexURLPattern(LocaleRegexProvider):
    callback = ...  # type: Callable[..., HttpResponse]
    default_args = ...  # type: Params
    name = ...  # type: Optional[str]
    def __init__(self, regex: str, callback: Callable[..., HttpResponse], default_args: Params=None, name: str=None) -> None: ...
    def resolve(self, path: str) -> ResolverMatch: ...
    def lookup_str(self) -> str: ...

class RegexURLResolver(LocaleRegexProvider):
    urlconf_name = ...  # type: URLConf
    default_kwargs = ...  # type: Params
    namespace = ...  # type: Optional[str]
    app_name = ...  # type: Optional[str]
    def __init__(self, regex: Optional[str], urlconf_name: URLConf, default_kwargs: Params=None, app_name: str=None, namespace: str=None) -> None: ...
    @property
    def reverse_dict(self) -> ReverseLookup: ...
    @property
    def namespace_dict(self) -> Namespace: ...
    @property
    def app_dict(self) -> AppDict: ...
    def resolve(self, path: str) -> ResolverMatch: ...
    def urlconf_module(self) -> Union[Iterable[URLPattern], Any]: ...
    def url_patterns(self) -> Iterable[URLPattern]: ...
    def resolve_error_handler(self, view_type: int) -> Tuple[Callable, Params]: ...
    def reverse(self, lookup_view: str, *args: object, **kwargs: object) -> str: ...

class LocaleRegexURLResolver(RegexURLResolver):
    prefix_default_language = ...  # type: bool
    def __init__(self, urlconf_name: URLConf, default_kwargs: Params=None, app_name: str=None, namespace: str=None, prefix_default_language: bool=True) -> None: ...
    @property
    def regex(self) -> Pattern[str]: ...
