from django.core.management.base import BaseCommand
from django.utils import timezone
from data import *


class Command(BaseCommand):
	print('start insert data in DB')
	print('----------------------')
	def handle(self, *args, **kwargs):
		for job in jobs:
			print(job)
			print('***')
		print('----------------------')
		print('end insert data in DB')