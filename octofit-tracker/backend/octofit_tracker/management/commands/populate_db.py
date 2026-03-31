from django.core.management.base import BaseCommand
from octofit_tracker import models
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        models.Team.objects.all().delete()
        models.Activity.objects.all().delete()
        models.Leaderboard.objects.all().delete()
        models.Workout.objects.all().delete()
        User.objects.all().delete()

        # Create Teams
        marvel = models.Team.objects.create(name='Marvel')
        dc = models.Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Create Activities
        models.Activity.objects.create(user=ironman, type='run', duration=30)
        models.Activity.objects.create(user=batman, type='cycle', duration=45)

        # Create Workouts
        models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes')
        models.Workout.objects.create(name='Strength Training', description='Strength for all heroes')


        # Create Leaderboard (team-based)
        models.Leaderboard.objects.create(team=marvel, points=190)  # sum of marvel users
        models.Leaderboard.objects.create(team=dc, points=180)  # sum of dc users

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
