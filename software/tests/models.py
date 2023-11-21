from django.test import TestCase
from django.template.defaultfilters import slugify
from software.models import Category, Tag, License, Software


# Create your tests here.
# Test data
app_path = "/software"
app_path_tag = f"{app_path}/tags"
app_path_category = f"{app_path}/categories"
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

test_software_sample_data = {
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
    # Test for model creation
    @classmethod
    def setUpTestData(cls):
        cls.test_tag_sample_one = Tag.objects.create(**test_tag_sample_data)
        cls.test_category_sample_one = Category.objects.create(
            **test_category_sample_data
        )
        cls.test_license_sample_one = License.objects.create(**test_license_sample_data)
        cls.test_software_sample_one = Software.objects.create(
            **test_software_sample_data["one"]
        )
        test_software_sample_two = Software.objects.create(
            **test_software_sample_data["two"]
        )
        cls.test_software_sample_one.tags.set([cls.test_tag_sample_one.id])
        cls.test_software_sample_one.category.set([cls.test_category_sample_one.id])
        cls.test_software_sample_one.alternatives.set([test_software_sample_two.id])
        cls.test_software_sample_one.license = cls.test_license_sample_one  # type: ignore

    # Test for model return string
    def test_model_str(self):
        self.assertEqual(str(self.test_tag_sample_one), test_tag_sample_data["name"])
        self.assertEqual(
            str(self.test_category_sample_one), test_category_sample_data["name"]
        )
        self.assertEqual(
            str(self.test_license_sample_one), test_license_sample_data["name"]
        )
        self.assertEqual(
            str(self.test_software_sample_one),
            f"{test_software_sample_data['one']['name']} | {test_software_sample_data['one']['is_foss']}",
        )

    # Test for get_absolute_url
    def test_model_get_absolute_url(self):
        self.assertEqual(
            f"{app_path_tag}/{test_tag_sample_data['slug']}/",
            self.test_tag_sample_one.get_absolute_url(),
        )
        self.assertEqual(
            f"{app_path_category}/{test_category_sample_data['slug']}/",
            self.test_category_sample_one.get_absolute_url(),
        )
        self.assertEqual(
            f"{app_path}/{test_software_sample_data['one']['slug']}/",
            self.test_software_sample_one.get_absolute_url(),
        )
