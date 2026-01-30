from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Team')
        dc = Team.objects.create(name='DC', description='DC Team')

        # Create users
        users = [
            User(email='ironman@marvel.com', username='Iron Man', team=marvel),
            User(email='spiderman@marvel.com', username='Spider-Man', team=marvel),
            User(email='captainamerica@marvel.com', username='Captain America', team=marvel),
            User(email='batman@dc.com', username='Batman', team=dc),
            User(email='superman@dc.com', username='Superman', team=dc),
            User(email='wonderwoman@dc.com', username='Wonder Woman', team=dc),
        ]
        for user in users:
            user.save()

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Upper body strength', difficulty='Easy'),
            Workout(name='Running', description='Cardio', difficulty='Medium'),
            Workout(name='Squats', description='Lower body strength', difficulty='Easy'),
        ]
        for workout in workouts:
            workout.save()

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Pushups', duration=30, date='2023-01-01'),
            Activity(user=users[1], activity_type='Running', duration=45, date='2023-01-02'),
            Activity(user=users[3], activity_type='Squats', duration=20, date='2023-01-03'),
        ]
        for activity in activities:
            activity.save()

        # Create leaderboard
        leaderboard_entries = [
            Leaderboard(user=users[0], score=100, rank=1),
            Leaderboard(user=users[1], score=90, rank=2),
            Leaderboard(user=users[3], score=80, rank=3),
        ]
        for entry in leaderboard_entries:
            entry.save()

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
