#!/usr/bin/env python
# coding: utf-8

CUR_ENV=''

if os.environ.has_key("IDCDEPLOY_ENV") and os.environ["IDCDEPLOY_ENV"] == "production":
    # product environment

    CUR_ENV='PRO'

else:
    # develop environment

    CUR_ENV='PRE'
