#!/usr/bin/env python3
"""Measure declared plain UI copy; counts do not establish semantic completeness."""
import argparse,json,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('input',type=Path,help='JSON list: id, mode(rewrite/new), before(if rewrite), after, max_chars(if new), optional exception{reason,required_meaning}')
a=p.parse_args()
rows=json.loads(a.input.read_text())
def count(text):return sum(not char.isspace() for char in text)
results=[]
for row in rows:
 after=count(row['after']);mode=row['mode']
 if mode=='rewrite':
  before=count(row['before'])
  if before==0:raise ValueError('Empty original: use new mode with a numeric budget')
  within=after*5<=before*4
  measure={'before_chars':before,'after_chars':after,'ratio':after/before,'limit_ratio':0.8}
 elif mode=='new':
  budget=row['max_chars']
  if not isinstance(budget,int) or budget<=0:raise ValueError('New copy needs a positive integer max_chars')
  within=after<=budget;measure={'after_chars':after,'max_chars':budget}
 else:raise ValueError('mode must be rewrite or new')
 exception=row.get('exception',{})
 justified=bool(str(exception.get('reason','')).strip() and str(exception.get('required_meaning','')).strip())
 status='within_limit' if within else 'exception_for_review' if justified else 'over_limit'
 results.append({'id':row['id'],'mode':mode,**measure,'numeric_result':status,'exception':exception if justified and not within else None,'meaning_preservation':'requires_content_review'})
print(json.dumps({'counting':'Unicode non-whitespace characters, including punctuation; plain visible text only','items':results,'over_limit':sum(x['numeric_result']=='over_limit' for x in results),'exceptions':sum(x['numeric_result']=='exception_for_review' for x in results),'claim':'Numeric measurement only. Exceptions are not numerical passes; semantic completeness requires review.'},ensure_ascii=False,indent=2))
sys.exit(1 if any(x['numeric_result']=='over_limit' for x in results) else 0)
