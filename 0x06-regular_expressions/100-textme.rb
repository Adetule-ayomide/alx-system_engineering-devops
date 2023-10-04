#!/usr/bin/env ruby
log_data = ARGV[0]
from_info = log_data.scan(/from:(\+?\d+|[a-zA-Z]+)/).flatten.join(",")
to_info = log_data.scan(/to:(\+?\d+|[a-zA-Z]+)/).flatten.join(",")
flags_info = log_data.scan(/flags:(\S+\d+)/).flatten.join(",")

puts "#{from_info},#{to_info},#{flags_info}"
