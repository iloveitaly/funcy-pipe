from typing import Any, Callable

def patch(): ...

def accumulate(iterable, *, initial): ...

def all(pred: Callable): ...

def all_fn(*fs): ...

def any(pred: Callable): ...

def any_fn(*fs): ...

def autocurry(func: Callable, _spec, _args, _kwargs): ...

def butlast(seq): ...

def cache(timeout): ...

def cached_property(fget): ...

def cached_readonly(fget): ...

def caller(*a): ...

def cat(iterable, /): ...

def chain(*args): ...

def chunks(n: int, seq): ...

def collecting(call): ...

def compact(coll): ...

def complement(pred: Callable): ...

def compose(*fs): ...

def concat(*args): ...

def constantly(x): ...

def contextmanager(func: Callable): ...

def count(start=0): ...

def count_by(f: Callable): ...

def count_reps(seq): ...

def curry(func: Callable, n: int): ...

def cut_prefix(s): ...

def cut_suffix(s): ...

def cycle(iterable, /): ...

def dec(x): ...

def decorator(deco): ...

def del_in(coll): ...

def distinct(seq): ...

def drop(n: int): ...

def dropwhile(pred: Callable): ...

def empty(): ...

def even(x): ...

def fallback(*approaches): ...

def filter(pred: Callable): ...

def first(seq): ...

def flatten(seq): ...

def flip(mapping): ...

def func_partial(func: Callable, **kwargs): ...

def get_in(coll, path, default): ...

def get_lax(coll, default): ...

def group_by(f: Callable): ...

def group_by_keys(get_keys): ...

def group_values(seq): ...

def has_path(coll): ...

def identity(x): ...

def iffy(pred: Callable, default): ...

def ignore(errors): ...

def ilen(seq): ...

def inc(x): ...

def interleave(*seqs): ...

def interpose(sep): ...

def invoke(objects, *args, **kwargs): ...

def is_distinct(coll): ...

def is_iter(x): ...

def is_list(x): ...

def is_mapping(x): ...

def is_seq(x): ...

def is_seqcoll(x): ...

def is_seqcont(x): ...

def is_set(x): ...

def is_tuple(x): ...

def isa(*types): ...

def isnone(x): ...

def iterable(x): ...

def iterate(f: Callable): ...

def iteritems(): ...

def itervalues(): ...

def join(colls): ...

def join_with(f: Callable, strict): ...

def joining(call): ...

def juxt(*fs): ...

def keep(f: Callable): ...

def last(seq): ...

def lcat(seqs): ...

def lchunks(n: int, seq): ...

def lconcat(*seqs): ...

def ldistinct(seq): ...

def lfilter(pred: Callable): ...

def lflatten(seq): ...

def limit_error_rate(fails, exception): ...

def linvoke(objects, *args, **kwargs): ...

def ljuxt(*fs): ...

def lkeep(f: Callable): ...

def lmap(f: Callable): ...

def lmapcat(f: Callable): ...

def log_calls(call, errors, stack, repr_len): ...

def log_durations(print_func, unit, threshold, repr_len): ...

def log_enters(call, repr_len): ...

def log_errors(print_func, stack, repr_len): ...

def log_exits(call, errors, stack, repr_len): ...

def log_iter_durations(seq, label, unit): ...

def lpartition(n: int, seq): ...

def lpartition_by(f: Callable): ...

def lpluck(key): ...

def lpluck_attr(attr): ...

def lreductions(f: Callable, acc): ...

def lremove(pred: Callable): ...

def lsplit(pred: Callable): ...

def lsplit_at(n: int): ...

def lsplit_by(pred: Callable): ...

def lsums(seq): ...

def ltree_leaves(root, children): ...

def ltree_nodes(root, children): ...

def lwhere(mappings): ...

def lwithout(seq): ...

def lzip(*seqs): ...

def make_lookuper(func: Callable): ...

def map(f: Callable): ...

def mapcat(f: Callable): ...

def memoize(_func=None): ...

def merge(*colls): ...

def merge_with(f: Callable): ...

def monkey(cls): ...

def none(pred: Callable): ...

def none_fn(*fs): ...

def notnone(x): ...

def nth(n: int): ...

def nullcontext(enter_result=None): ...

def odd(x): ...

def omit(keys): ...

def once(func: Callable): ...

def once_per(*argnames): ...

def once_per_args(func: Callable): ...

def one(pred: Callable): ...

def one_fn(*fs): ...

def pairwise(seq): ...

def partial(*args, **kwargs): ...

def partition(n: int, seq): ...

def partition_by(f: Callable): ...

def pluck(key): ...

def pluck_attr(attr): ...

def post_processing(call): ...

def print_calls(errors=True, repr_len=25): ...

def print_durations(label=None): ...

def print_enters(repr_len=25): ...

def print_errors(label=None): ...

def print_exits(errors=True, repr_len=25): ...

def print_iter_durations(seq, unit): ...

def project(mapping): ...

def raiser(exception_or_class, **kwargs): ...

def rcompose(*fs): ...

def rcurry(func: Callable, n: int): ...

def re_all(regex: str, flags): ...

def re_find(regex: str, flags): ...

def re_finder(regex: str): ...

def re_iter(regex: str, flags): ...

def re_test(regex: str, flags): ...

def re_tester(regex: str): ...

def reductions(f: Callable, acc): ...

def remove(pred: Callable): ...

def repeat(*args): ...

def repeatedly(f: Callable): ...

def reraise(errors): ...

def rest(seq): ...

def retry(call, errors, timeout, filter_errors): ...

def rpartial(func: Callable, *args, **kwargs): ...

def second(seq): ...

def select(pred: Callable): ...

def select_keys(pred: Callable): ...

def select_values(pred: Callable): ...

def set_in(coll, value): ...

def silent(func: Callable): ...

def silent_lookuper(func: Callable): ...

def some(pred: Callable): ...

def some_fn(*fs): ...

def split(pred: Callable): ...

def split_at(n: int): ...

def split_by(pred: Callable): ...

def str_join(sep): ...

def sums(seq): ...

def suppress(*exceptions): ...

def take(n: int): ...

def takewhile(pred: Callable): ...

def tap(x): ...

def throttle(period): ...

def tree_leaves(root, children): ...

def tree_nodes(root, children): ...

def unwrap(func: Callable): ...

def update_in(coll, update, default): ...

def walk(f: Callable): ...

def walk_keys(f: Callable): ...

def walk_values(f: Callable): ...

def where(mappings): ...

def with_next(seq): ...

def with_prev(seq): ...

def without(seq): ...

def wrap_prop(ctx): ...

def wrap_with(call): ...

def wraps(wrapped, updated): ...

def zip_dicts(*dicts): ...

def zip_values(*dicts): ...

def zipdict(keys): ...

def to_list(): ...

def log(): ...

def bp(): ...

def exactly_one(comprehension): ...

def pipe(func: Callable): ...

def reduce(func: Callable, initial): ...

def pmap(func: Callable): ...
