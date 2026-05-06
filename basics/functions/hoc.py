def instance_fn(cb):
    def wrapper_fn():
        print("*" * 10)
        cb();
        print("*" * 10)
    return wrapper_fn;

def hello():
    print('Hello Python')

hello_instance = instance_fn(hello);
hello_instance();