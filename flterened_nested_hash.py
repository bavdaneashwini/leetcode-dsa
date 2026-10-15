
input_dict = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip": "10001",
        "location": {
            "country": "USA",
            "coordinates": {
                "latitude": 40.7128,
                "longitude": -74.0060
            }
        }
    }
}


#Python function to flatten a nested dictionary

def flat_hash(input_hash,prefix_value=""):
    flat_dict={}
    for key, value in input_hash.items():
        new_key = prefix_value+"."+key if prefix_value else key
    if isinstance(value,dict):
        flat_dict.update(flat_hash(value,new_key))
    else:
        flat_dict[new_key]=value

    return flat_dict

hash = flat_hash(input_dict)
print(hash)    




input_hash = {
  "name" => "John",
  "age" => 30,
  "address" => {
    "street" => "123 Main St",
    "city" => "New York",
    "state" => "NY",
    "zip" => "10001",
    "location" => {
      "country" => "USA",
      "coordinates" => {
        "latitude" => 40.7128,
        "longitude" => -74.0060
      }
    }
  }
}

#Ruby function to flatten a nested hash

def flatten_hash(input_hash, prefix = "")
  flattened = {}

  input_hash.each do |key, value|
    new_key = prefix.empty? ? key : "#{prefix}.#{key}"

    if value.is_a?(Hash)
      flattened.merge!(flatten_hash(value, new_key))
    else
      flattened[new_key] = value
    end
  end

  flattened
end

result = flatten_hash(input_hash)
puts result


