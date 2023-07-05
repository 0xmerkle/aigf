```python
from django.test import TestCase
from .models import MyModel

class MyModelTestCase(TestCase):
    def setUp(self):
        MyModel.objects.create(name="test1")
        MyModel.objects.create(name="test2")

    def test_my_model_name(self):
        model1 = MyModel.objects.get(name="test1")
        model2 = MyModel.objects.get(name="test2")
        self.assertEqual(model1.name, 'test1')
        self.assertEqual(model2.name, 'test2')
```