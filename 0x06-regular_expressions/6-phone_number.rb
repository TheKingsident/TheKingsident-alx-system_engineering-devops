#!/usr/bin/env ruby
puts ARGV[0].scan(/^\s?(\d{3}[-\s]?\d{3}[-\s]?\d{4})$/).join
