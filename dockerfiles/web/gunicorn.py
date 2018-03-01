import multiprocessing

bind = '0.0.0.0:8000'

# You can customize here to the gunicore recomended workers amount
# workers = multiprocessing.cpu_count() * 2
workers = 2
