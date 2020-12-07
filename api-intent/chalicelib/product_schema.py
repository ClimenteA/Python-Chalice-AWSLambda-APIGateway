from jsonschema import validate


schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "productId": 42,
            "sku": "QWEQWEW-42",
            "productName": "Ultimate killer v3.0 | CI ltd.",
            "price": {
                "productPrice": "35.8 GBP",
                "priceCurrency": "British Pound"
            },
            "details": {
                "productDescription": "A very good product",
                "powerRequired": "a lot",
                "productKeywords": "chalice, serverless, python"
            },
            "media": {
                "images": [
                    "",
                    ""
                ]
            },
            "category": "some category",
            "brand": "CI ltd.",
            "ratings": {
                "avgRating": "5",
                "ratingCount": "5",
                "ratedSince": "5655-53-24 09:15:00"
            },
            "availabilty": {
                "stage": "Beta",
                "status": "Pre-order"
            },
            "dateAdded": "1955-11-05 22:04:00"
        }
    ],
    "required": [
        "productId",
        "sku",
        "productName",
        "price",
        "details",
        "media",
        "category",
        "brand",
        "ratings",
        "availabilty",
        "dateAdded"
    ],
    "properties": {
        "productId": {
            "$id": "#/properties/productId",
            "type": "integer",
            "title": "The productId schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                42
            ]
        },
        "sku": {
            "$id": "#/properties/sku",
            "type": "string",
            "title": "The sku schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "QWEQWEW-42"
            ]
        },
        "productName": {
            "$id": "#/properties/productName",
            "type": "string",
            "title": "The productName schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "Ultimate killer v3.0 | CI ltd."
            ]
        },
        "price": {
            "$id": "#/properties/price",
            "type": "object",
            "title": "The price schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "productPrice": "35.8 GBP",
                    "priceCurrency": "British Pound"
                }
            ],
            "required": [
                "productPrice",
                "priceCurrency"
            ],
            "properties": {
                "productPrice": {
                    "$id": "#/properties/price/properties/productPrice",
                    "type": "string",
                    "title": "The productPrice schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "35.8 GBP"
                    ]
                },
                "priceCurrency": {
                    "$id": "#/properties/price/properties/priceCurrency",
                    "type": "string",
                    "title": "The priceCurrency schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "British Pound"
                    ]
                }
            },
            "additionalProperties": True
        },
        "details": {
            "$id": "#/properties/details",
            "type": "object",
            "title": "The details schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "productDescription": "A very good product",
                    "powerRequired": "a lot",
                    "productKeywords": "chalice, serverless, python"
                }
            ],
            "required": [
                "productDescription",
                "powerRequired",
                "productKeywords"
            ],
            "properties": {
                "productDescription": {
                    "$id": "#/properties/details/properties/productDescription",
                    "type": "string",
                    "title": "The productDescription schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "A very good product"
                    ]
                },
                "powerRequired": {
                    "$id": "#/properties/details/properties/powerRequired",
                    "type": "string",
                    "title": "The powerRequired schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "a lot"
                    ]
                },
                "productKeywords": {
                    "$id": "#/properties/details/properties/productKeywords",
                    "type": "string",
                    "title": "The productKeywords schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "chalice, serverless, python"
                    ]
                }
            },
            "additionalProperties": True
        },
        "media": {
            "$id": "#/properties/media",
            "type": "object",
            "title": "The media schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "images": [
                        "",
                        ""
                    ]
                }
            ],
            "required": [
                "images"
            ],
            "properties": {
                "images": {
                    "$id": "#/properties/media/properties/images",
                    "type": "array",
                    "title": "The images schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": [],
                    "examples": [
                        [
                            "",
                            ""
                        ]
                    ],
                    "additionalItems": True,
                    "items": {
                        "$id": "#/properties/media/properties/images/items",
                        "anyOf": [
                            {
                                "$id": "#/properties/media/properties/images/items/anyOf/0",
                                "type": "string",
                                "title": "The first anyOf schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    ""
                                ]
                            }
                        ]
                    }
                }
            },
            "additionalProperties": True
        },
        "category": {
            "$id": "#/properties/category",
            "type": "string",
            "title": "The category schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "some category"
            ]
        },
        "brand": {
            "$id": "#/properties/brand",
            "type": "string",
            "title": "The brand schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "CI ltd."
            ]
        },
        "ratings": {
            "$id": "#/properties/ratings",
            "type": "object",
            "title": "The ratings schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "avgRating": "5",
                    "ratingCount": "5",
                    "ratedSince": "5655-53-24 09:15:00"
                }
            ],
            "required": [
                "avgRating",
                "ratingCount",
                "ratedSince"
            ],
            "properties": {
                "avgRating": {
                    "$id": "#/properties/ratings/properties/avgRating",
                    "type": "string",
                    "title": "The avgRating schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "5"
                    ]
                },
                "ratingCount": {
                    "$id": "#/properties/ratings/properties/ratingCount",
                    "type": "string",
                    "title": "The ratingCount schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "5"
                    ]
                },
                "ratedSince": {
                    "$id": "#/properties/ratings/properties/ratedSince",
                    "type": "string",
                    "title": "The ratedSince schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "5655-53-24 09:15:00"
                    ]
                }
            },
            "additionalProperties": True
        },
        "availabilty": {
            "$id": "#/properties/availabilty",
            "type": "object",
            "title": "The availabilty schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "stage": "Beta",
                    "status": "Pre-order"
                }
            ],
            "required": [
                "stage",
                "status"
            ],
            "properties": {
                "stage": {
                    "$id": "#/properties/availabilty/properties/stage",
                    "type": "string",
                    "title": "The stage schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "Beta"
                    ]
                },
                "status": {
                    "$id": "#/properties/availabilty/properties/status",
                    "type": "string",
                    "title": "The status schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "Pre-order"
                    ]
                }
            },
            "additionalProperties": True
        },
        "dateAdded": {
            "$id": "#/properties/dateAdded",
            "type": "string",
            "title": "The dateAdded schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "1955-11-05 22:04:00"
            ]
        }
    },
    "additionalProperties": True
}


def productSchemaIsValid(product_json):
    try:
        validate(instance=product_json, schema=schema)
        return True
    except:
        return False


# json_data_example = {
#     "productId": 42, 
#     "sku": "QWEQWEW-42", 
#     "productName": "Ultimate killer v3.0 | CI ltd.", 
#     "price": {
#         "productPrice": "35.8 GBP", 
#         "priceCurrency": "British Pound"
#     }, 

#     "details": {
#         "productDescription": "A very good product", 
#         "powerRequired": "a lot", 
#         "productKeywords": "chalice, serverless, python"
#     }, 
    
#     "media": {"images": ["", ""]}, 
#     "category": "some category", 
#     "brand": "CI ltd.", 
    
#     "ratings": {
#         "avgRating": "5", 
#         "ratingCount": "5", 
#         "ratedSince": "5655-53-24 09:15:00"
#     }, 

#     "availabilty": {
#         "stage": "Beta", 
#         "status": "Pre-order"
#     }, 
    
#     "dateAdded": "1955-11-05 22:04:00"
# }