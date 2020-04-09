#!/usr/bin/env python

import argparse

from jeep.maintenance import GreaseJob

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Schedules a grease job.')
    parser.add_argument('account_token', type=str, help='A github account token.')
    args = parser.parse_args()

    # Schedule the job.
    g = GreaseJob(account_token=args.account_token)
    g.run()
