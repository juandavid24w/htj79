from django.test import TestCase
from django.template.defaultfilters import slugify
from software.models import Category, Tag, License, Software


# Create your tests here.
test_category_sample_data = {
    "name": "Test Category Sample One",
    "slug": slugify("Test Category Sample One"),
}

test_tag_sample_data = {
    "name": "Test Tag Sample One",
    "slug": slugify("Test Tag Sample One"),
}

test_license_sample_data = {
    "name": "Test License Sample One",
}

test_software_sample_date = {
    "one": {
        "name": "Test Software Sample One",
        "slug": slugify("Test Software Sample One"),
        "is_foss": True,
    },
    "two": {
        "name": "Test Software Sample Two",
        "slug": slugify("Test Software Sample Two"),
        "is_foss": False,
    },
}


class TestSoftwareModels(TestCase):
    def test_model_str(self):
        test_tag_sample_one = Tag.objects.create(**test_tag_sample_data)
        self.assertEqual(str(test_tag_sample_one), test_tag_sample_data["name"])
        test_category_sample_one = Category.objects.create(**test_category_sample_data)
        self.assertEqual(
            str(test_category_sample_one), test_category_sample_data["name"]
        )
        test_license_sample_one = License.objects.create(**test_license_sample_data)
        self.assertEqual(str(test_license_sample_one), test_license_sample_data["name"])
        test_software_sample_one = Software.objects.create(
            **test_software_sample_date["one"]
        )
        test_software_sample_one.tags.set([test_tag_sample_one.id])
        test_software_sample_one.category.set([test_category_sample_one.id])
        test_software_sample_one.license = test_license_sample_one  # type: ignore
        self.assertEqual(
            str(test_software_sample_one),
            f"{test_software_sample_date['one']['name']} | {test_software_sample_date['one']['is_foss']}",
        )
