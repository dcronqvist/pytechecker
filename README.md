# pytechecker
✔️ A small uility Python module for type checking an object towards a sample object.

## Getting started

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
Here we have defined a sample object which would allow any object that has a key `name`, which is required to exist and must be a string. There is however also an optional key `age` which must be of the type int. If we were to check an object like this:

```python
{
    "name": "Daniel",
    "age": 21
}
```
against the sample object, there would be **no complaints**, but there wouldn't be any complaints on an object like this either:

```python
{
    "name": "Daniel"
}
```
This is because of the fact that the key `age` is optional, and can be omitted.
