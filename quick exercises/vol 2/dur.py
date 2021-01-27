def what_is(x): return 'everything' if x == 42 else 'everything squared' if x == 42 * 42 else 'nothing'
def what_is(x): return {42 * 42: 'everything squared', 42: 'everything'}.get(x, 'nothing')