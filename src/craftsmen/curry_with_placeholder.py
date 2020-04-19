from . import setup, find_packages

from .placeholder import p

class _Placeholders():
  def __init__(self, args):
    self.args = args
    self.len = len(_filter_placeholder(args))

def _filter_placeholder(args):
    return tuple(v for v in args if v is not p)

def _concat_args(placeholders, args):
    args.reverse()
    get_arg = lambda v: args.pop() if v is p else v
    return tuple([get_arg(v) for v in placeholders.args] + args)

def _check_len(args_count, placeholders, args):
    args_len = len(args) + placeholders.len
    return args_len >= args_count

def _curry_builder(function, args_count, placeholders=None, memo_args=()):
    if placeholders is None:
        def dummie_initializer(*args)
            dummie = _curry_builder(
                function,
                args_count,
                placeholders=_Placeholders(args),
                memo_args=_filter_placeholder(args),
            )
            return dummie(*args)
        return dummie_initializer

    def dummie(*args):
        new_args = memo_args + args
        if _check_len(args_count, placeholders, args=new_args):
            new_args = _concat_args(placeholders, args=list(new_args))
            return function(*new_args)
        else:
            return _curry_builder(
                function,
                args_count,
                placeholders,
                memo_args=new_args,
            )
    return dummie

def curry(function):
    args_count = function.__code__.co_argcount
    # args_names = function.__code__.co_varnames
    return _curry_builder(
        function,
        args_count,
    )
