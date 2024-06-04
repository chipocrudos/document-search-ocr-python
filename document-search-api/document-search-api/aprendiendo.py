from config.configuration import zincConfig, s3Config
import httpx
import boto3


minio = boto3.client( # type: ignore
        s3Config.SERVICE_NAME, # type: ignore
        endpoint_url=s3Config.ENDPOINT_URL,
        aws_access_key_id=s3Config.ACCESS_KEY,
        aws_secret_access_key=s3Config.SECRET_KEY
    ) # type: ignore



# curl http://localhost:4080/api/index_name?name= -i -u admin:strong3xample
# curl http://localhost:4080/api/index/manuales  -i -u admin:strong3xample
HEADERS = {
    "Content-type": "application/json",
    "Authorization": f"Basic {zincConfig.ZINC_CRED}"
}

paramsv2= {
     "_source": [
    "string"
  ],
  "aggs": {
    "additionalProp1": {
      "aggs": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "auto_date_histogram": {
        "buckets": 0,
        "field": "string",
        "format": "string",
        "keyed": True,
        "minimum_interval": "string",
        "time_zone": "string"
      },
      "avg": {
        "field": "string",
        "weight_field": "string"
      },
      "cardinality": {
        "field": "string",
        "weight_field": "string"
      },
      "count": {
        "field": "string",
        "weight_field": "string"
      },
      "date_histogram": {
        "calendar_interval": "string",
        "extended_bounds": {
          "max": 0,
          "min": 0
        },
        "field": "string",
        "fixed_interval": "string",
        "format": "string",
        "hard_bounds": {
          "max": 0,
          "min": 0
        },
        "interval": "string",
        "keyed": True,
        "min_doc_count": 0,
        "size": 0,
        "time_zone": "string"
      },
      "date_range": {
        "field": "string",
        "format": "string",
        "keyed": True,
        "ranges": [
          {
            "from": "string",
            "to": "string"
          }
        ],
        "time_zone": "string"
      },
      "histogram": {
        "extended_bounds": {
          "max": 0,
          "min": 0
        },
        "field": "string",
        "hard_bounds": {
          "max": 0,
          "min": 0
        },
        "interval": 0,
        "keyed": True,
        "min_doc_count": 0,
        "offset": 0,
        "size": 0
      },
      "ip_range": {
        "field": "string",
        "keyed": True,
        "ranges": [
          {
            "from": "string",
            "to": "string"
          }
        ]
      },
      "max": {
        "field": "string",
        "weight_field": "string"
      },
      "min": {
        "field": "string",
        "weight_field": "string"
      },
      "range": {
        "field": "string",
        "keyed": True,
        "ranges": [
          {
            "from": 0,
            "to": 0
          }
        ]
      },
      "sum": {
        "field": "string",
        "weight_field": "string"
      },
      "terms": {
        "field": "string",
        "order": {
          "additionalProp1": "string",
          "additionalProp2": "string",
          "additionalProp3": "string"
        },
        "size": 0
      },
      "weighted_avg": {
        "field": "string",
        "weight_field": "string"
      }
    },
    "additionalProp2": {
      "aggs": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "auto_date_histogram": {
        "buckets": 0,
        "field": "string",
        "format": "string",
        "keyed": True,
        "minimum_interval": "string",
        "time_zone": "string"
      },
      "avg": {
        "field": "string",
        "weight_field": "string"
      },
      "cardinality": {
        "field": "string",
        "weight_field": "string"
      },
      "count": {
        "field": "string",
        "weight_field": "string"
      },
      "date_histogram": {
        "calendar_interval": "string",
        "extended_bounds": {
          "max": 0,
          "min": 0
        },
        "field": "string",
        "fixed_interval": "string",
        "format": "string",
        "hard_bounds": {
          "max": 0,
          "min": 0
        },
        "interval": "string",
        "keyed": True,
        "min_doc_count": 0,
        "size": 0,
        "time_zone": "string"
      },
      "date_range": {
        "field": "string",
        "format": "string",
        "keyed": True,
        "ranges": [
          {
            "from": "string",
            "to": "string"
          }
        ],
        "time_zone": "string"
      },
      "histogram": {
        "extended_bounds": {
          "max": 0,
          "min": 0
        },
        "field": "string",
        "hard_bounds": {
          "max": 0,
          "min": 0
        },
        "interval": 0,
        "keyed": True,
        "min_doc_count": 0,
        "offset": 0,
        "size": 0
      },
      "ip_range": {
        "field": "string",
        "keyed": True,
        "ranges": [
          {
            "from": "string",
            "to": "string"
          }
        ]
      },
      "max": {
        "field": "string",
        "weight_field": "string"
      },
      "min": {
        "field": "string",
        "weight_field": "string"
      },
      "range": {
        "field": "string",
        "keyed": True,
        "ranges": [
          {
            "from": 0,
            "to": 0
          }
        ]
      },
      "sum": {
        "field": "string",
        "weight_field": "string"
      },
      "terms": {
        "field": "string",
        "order": {
          "additionalProp1": "string",
          "additionalProp2": "string",
          "additionalProp3": "string"
        },
        "size": 0
      },
      "weighted_avg": {
        "field": "string",
        "weight_field": "string"
      }
    },
    "additionalProp3": {
      "aggs": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      },
      "auto_date_histogram": {
        "buckets": 0,
        "field": "string",
        "format": "string",
        "keyed": True,
        "minimum_interval": "string",
        "time_zone": "string"
      },
      "avg": {
        "field": "string",
        "weight_field": "string"
      },
      "cardinality": {
        "field": "string",
        "weight_field": "string"
      },
      "count": {
        "field": "string",
        "weight_field": "string"
      },
      "date_histogram": {
        "calendar_interval": "string",
        "extended_bounds": {
          "max": 0,
          "min": 0
        },
        "field": "string",
        "fixed_interval": "string",
        "format": "string",
        "hard_bounds": {
          "max": 0,
          "min": 0
        },
        "interval": "string",
        "keyed": True,
        "min_doc_count": 0,
        "size": 0,
        "time_zone": "string"
      },
      "date_range": {
        "field": "string",
        "format": "string",
        "keyed": True,
        "ranges": [
          {
            "from": "string",
            "to": "string"
          }
        ],
        "time_zone": "string"
      },
      "histogram": {
        "extended_bounds": {
          "max": 0,
          "min": 0
        },
        "field": "string",
        "hard_bounds": {
          "max": 0,
          "min": 0
        },
        "interval": 0,
        "keyed": True,
        "min_doc_count": 0,
        "offset": 0,
        "size": 0
      },
      "ip_range": {
        "field": "string",
        "keyed": True,
        "ranges": [
          {
            "from": "string",
            "to": "string"
          }
        ]
      },
      "max": {
        "field": "string",
        "weight_field": "string"
      },
      "min": {
        "field": "string",
        "weight_field": "string"
      },
      "range": {
        "field": "string",
        "keyed": True,
        "ranges": [
          {
            "from": 0,
            "to": 0
          }
        ]
      },
      "sum": {
        "field": "string",
        "weight_field": "string"
      },
      "terms": {
        "field": "string",
        "order": {
          "additionalProp1": "string",
          "additionalProp2": "string",
          "additionalProp3": "string"
        },
        "size": 0
      },
      "weighted_avg": {
        "field": "string",
        "weight_field": "string"
      }
    }
  },
  "explain": True,
  "fields": [
    "string"
  ],
  "from": 0,
  "highlight": {
    "fields": {
      "additionalProp1": "string",
      "additionalProp2": "string",
      "additionalProp3": "string"
    },
    "fragment_size": 0,
    "number_of_fragments": 0,
    "post_tags": [
      "string"
    ],
    "pre_tags": [
      "string"
    ]
  },
  "query": {
    "bool": {
      "filter": [
        "string"
      ],
      "minimum_should_match": 0,
      "must": [
        "string"
      ],
      "must_not": [
        "string"
      ],
      "should": [
        "string"
      ]
    },
    "exists": {
      "field": "string"
    },
    "fuzzy": {
      "additionalProp1": {
        "boost": 0,
        "fuzziness": "string",
        "prefix_length": 0,
        "value": "string"
      },
      "additionalProp2": {
        "boost": 0,
        "fuzziness": "string",
        "prefix_length": 0,
        "value": "string"
      },
      "additionalProp3": {
        "boost": 0,
        "fuzziness": "string",
        "prefix_length": 0,
        "value": "string"
      }
    },
    "ids": {
      "values": [
        "string"
      ]
    },
    "match": {
      "additionalProp1": {
        "analyzer": "string",
        "boost": 0,
        "fuzziness": "string",
        "operator": "string",
        "prefix_length": 0,
        "query": "string"
      },
      "additionalProp2": {
        "analyzer": "string",
        "boost": 0,
        "fuzziness": "string",
        "operator": "string",
        "prefix_length": 0,
        "query": "string"
      },
      "additionalProp3": {
        "analyzer": "string",
        "boost": 0,
        "fuzziness": "string",
        "operator": "string",
        "prefix_length": 0,
        "query": "string"
      }
    },
    "match_all": {},
    "match_bool_prefix": {
      "additionalProp1": {
        "analyzer": "string",
        "boost": 0,
        "query": "string"
      },
      "additionalProp2": {
        "analyzer": "string",
        "boost": 0,
        "query": "string"
      },
      "additionalProp3": {
        "analyzer": "string",
        "boost": 0,
        "query": "string"
      }
    },
    "match_none": {},
    "match_phrase": {
      "additionalProp1": {
        "analyzer": "string",
        "boost": 0,
        "query": "string"
      },
      "additionalProp2": {
        "analyzer": "string",
        "boost": 0,
        "query": "string"
      },
      "additionalProp3": {
        "analyzer": "string",
        "boost": 0,
        "query": "string"
      }
    },
    "match_phrase_prefix": {
      "additionalProp1": {
        "analyzer": "string",
        "boost": 0,
        "query": "string"
      },
      "additionalProp2": {
        "analyzer": "string",
        "boost": 0,
        "query": "string"
      },
      "additionalProp3": {
        "analyzer": "string",
        "boost": 0,
        "query": "string"
      }
    },
    "multi_match": {
      "analyzer": "string",
      "boost": 0,
      "fields": [
        "string"
      ],
      "minimum_should_match": 0,
      "operator": "string",
      "query": "string",
      "type": "string"
    },
    "prefix": {
      "additionalProp1": {
        "boost": 0,
        "value": "string"
      },
      "additionalProp2": {
        "boost": 0,
        "value": "string"
      },
      "additionalProp3": {
        "boost": 0,
        "value": "string"
      }
    },
    "query_string": {
      "analyzer": "string",
      "boost": 0,
      "default_field": "string",
      "default_operator": "string",
      "fields": [
        "string"
      ],
      "query": "string"
    },
    "range": {
      "additionalProp1": {
        "boost": 0,
        "format": "string",
        "gt": "string",
        "gte": "string",
        "lt": "string",
        "lte": "string",
        "time_zone": "string"
      },
      "additionalProp2": {
        "boost": 0,
        "format": "string",
        "gt": "string",
        "gte": "string",
        "lt": "string",
        "lte": "string",
        "time_zone": "string"
      },
      "additionalProp3": {
        "boost": 0,
        "format": "string",
        "gt": "string",
        "gte": "string",
        "lt": "string",
        "lte": "string",
        "time_zone": "string"
      }
    },
    "regexp": {
      "additionalProp1": {
        "boost": 0,
        "flags": "string",
        "value": "string"
      },
      "additionalProp2": {
        "boost": 0,
        "flags": "string",
        "value": "string"
      },
      "additionalProp3": {
        "boost": 0,
        "flags": "string",
        "value": "string"
      }
    },
    "simple_query_string": {
      "all_fields": True,
      "analyzer": "string",
      "boost": 0,
      "default_operator": "string",
      "fields": [
        "string"
      ],
      "query": "string"
    },
    "term": {
      "additionalProp1": {
        "boost": 0,
        "case_insensitive": True,
        "value": "string"
      },
      "additionalProp2": {
        "boost": 0,
        "case_insensitive": True,
        "value": "string"
      },
      "additionalProp3": {
        "boost": 0,
        "case_insensitive": True,
        "value": "string"
      }
    },
    "terms": {
      "additionalProp1": {
        "additionalProp1": {}
      },
      "additionalProp2": {
        "additionalProp1": {}
      },
      "additionalProp3": {
        "additionalProp1": {}
      }
    },
    "wildcard": {
      "additionalProp1": {
        "boost": 0,
        "value": "string"
      },
      "additionalProp2": {
        "boost": 0,
        "value": "string"
      },
      "additionalProp3": {
        "boost": 0,
        "value": "string"
      }
    }
  },
  "size": 0,
  "sort": [
    "string"
  ],
  "timeout": 0,
  "track_total_hits": True
}

# params = {
#    "query": {
#     "match_pharse": {
#       "content": "martillo mesa madera"
#     }
#     }
# }

params = {
    "_source": [
    ],
    "query": {
        "match_pharse": "martillo mesa",
    },
    "track_total_hits": False

}



index="manuales"
print("-"*60)
print(zincConfig.get_index_search_api(index))

# r = httpx.get(
#     zincConfig.get_all_index_api(),
#     headers=HEADERS
# )

r = httpx.post(
    zincConfig.get_index_search_api(index),
    headers=HEADERS,
    json=params
)

if r.status_code != 200:
    print(r.status_code)
    print(r.text)
else:
    print(r.json()["hits"]["total"]["value"])

    for hit in r.json()["hits"]["hits"]:
        path = hit["_source"]["path"]
    


url = minio.generate_presigned_url(
    ClientMethod='get_object',
    Params={
        'Bucket': s3Config.BUCKET_NAME,
        'Key': path,
    },
    ExpiresIn=3600
)

print(url)
