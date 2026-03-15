from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Team Marvel')
        dc = app_models.Team.objects.create(name='Team DC')

        # Create Users
        tony = User.objects.create_user(username='ironman', email='tony@marvel.com', password='password', first_name='Tony', last_name='Stark', team=marvel)
        steve = User.objects.create_user(username='captain', email='steve@marvel.com', password='password', first_name='Steve', last_name='Rogers', team=marvel)
        bruce = User.objects.create_user(username='batman', email='bruce@dc.com', password='password', first_name='Bruce', last_name='Wayne', team=dc)
        clark = User.objects.create_user(username='superman', email='clark@dc.com', password='password', first_name='Clark', last_name='Kent', team=dc)

        # Create Activities
        app_models.Activity.objects.create(user=tony, type='Run', duration=30, calories=300)
        app_models.Activity.objects.create(user=steve, type='Swim', duration=45, calories=400)
        app_models.Activity.objects.create(user=bruce, type='Cycle', duration=60, calories=500)
        app_models.Activity.objects.create(user=clark, type='Fly', duration=120, calories=1000)

        # Create Workouts
        app_models.Workout.objects.create(name='Avengers HIIT', description='High intensity workout for Marvel heroes', suggested_for=marvel)
        app_models.Workout.objects.create(name='Justice League Strength', description='Strength workout for DC heroes', suggested_for=dc)

        # Create Leaderboard
        app_models.Leaderboard.objects.create(team=marvel, points=700)
        app_models.Leaderboard.objects.create(team=dc, points=1500)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
