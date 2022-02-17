import subprocess

# Run the spider synchronously:
subprocess.run(["scrapy", "crawl", "quotes", "-o", "quotes.json"])


# Run the spider asynchronously:
proc = subprocess.Popen(["scrapy", "crawl", "quotes", "-o", "quotes.json"])
print(proc.poll())
# None is returned is the job is still running.
# You can wait for the job to finish, or do something else in the
# meantime.
proc.wait()
print(proc.poll())
# 0 (exit code) is returned is the job is finished.
