# Copyright 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
import json
import os
import sys

from perf_insights.mre import job_results
from perf_insights.mre import failure
import perf_insights_project
import vinn

_REDUCE_MAP_RESULTS_CMDLINE_PATH = os.path.join(
  perf_insights_project.PerfInsightsProject.perf_insights_src_path,
  'mre', 'reduce_map_results_cmdline.html')


def ReduceMapResults(job_results, map_results_list, job):
  project = perf_insights_project.PerfInsightsProject()

  all_source_paths = list(project.source_paths)

  all_source_paths.append(project.perf_insights_root_path)

  js_args = [
    json.dumps([r.results for r in map_results_list]),
    json.dumps(job.AsDict()),
  ]

  res = vinn.RunFile(_REDUCE_MAP_RESULTS_CMDLINE_PATH,
                     source_paths=all_source_paths, js_args=js_args)

  results = job_results.JobResults.FromDict(json.loads(res.stdout))