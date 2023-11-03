#!/usr/bin/env ruby

match_data = ARGV[0].match(/\[from:(.+?)\] \[to:(.+?)\] \[flags:(.+?)\]/)

if match_data
  puts "#{match_data[1]},#{match_data[2]},#{match_data[3]}"
end

