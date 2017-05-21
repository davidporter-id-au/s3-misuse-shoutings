import os
import sys
sys.path.append(os.path.abspath(__file__ + "/../.."))
import receive_events

import unittest
import sample_events

class TestDetection(unittest.TestCase):

    def test_an_open_bucket(self):

        problems = receive_events.check_bucket_creation(
                sample_events.bucket_being_made_public_to_the_world,
                set()
            )
        self.assertEqual(problems[0]["error"], "Bucket is open for all users")
        self.assertEqual(problems[0]["error_title"], "Security warning for s3 bucket: some-bucket-name")
        self.assertEqual(problems[0]["bucket_name"], "some-bucket-name")
        self.assertEqual(problems[0]["person_responsible"], "some-principal:user@domain.org")

    def test_normal_bucket_creation_is_ok(self):

        problems = receive_events.check_bucket_creation(
                sample_events.bucket_is_cool,
                set()
            )

        self.assertEqual(problems, None)

    def test_bucket_is_whitelisted(self):

        problems = receive_events.check_bucket_creation(
                sample_events.bucket_being_made_public_to_the_world,
                set(["some-bucket-name"])
            )

        self.assertEqual(problems, None)


if __name__ == '__main__':
    unittest.main()
