# pytechecker
✔️ A small uility Python module for type checking an object towards a sample object.

![Tests](https://github.com/dcronqvist/pytechecker/workflows/Tests/badge.svg?branch=main)

## A simple example

Let's start by taking a look at a very simple sample object:

```python
{
    "name": {
        "required": True,
        "allowed_types": [str]
    },
    "age": {
        "required": False,
        "allowed_types": [int]
    }
}
```

Here we have defined a **sample object** which has one required key `name` and one optional key `age`. In the sample object we have also specified that the key `name` can only be of the type `str`, and `age` can only be an `int`. Let's see which objects that fit this sample.

```python
{
    "name": "Daniel",
    "age": 21
}
```

Above we have an object which fits the sample object. It's an object which has the required key `name` and the optional key `age`, and they both are their respective required types.

```python
{
    "name": "Daniel"
}
```

Above is an object that still fits the sample object. Since the key `age` is **optional**, we can omit it from the object without it causing it to be unfit.

```python
{
    "age": 21
}
```

The above object does, however, **NOT** fit the sample object. Upon attempting to match the object against the sample, you'll be met with the following error:

`ERROR: Key 'name' is required, but was absent in supplied object.`

We can also look at an example like this:

```python
{
    "name": "Daniel",
    "age": 21.4
}
```

The above object is unfit since one of its keys is of a type that is not allowed for that key. You'll be met with the following error:

`ERROR: On key 'age', expected one of ['int'], got float.`

So there we have it. That's a very simple example of how it works. 
