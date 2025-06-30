#!/usr/bin/env ruby

require 'date'

# Get the title from command line argument
if ARGV.empty?
  puts "Usage: ruby new_post.rb 'Your Post Title'"
  puts "This will create a markdown file that you can convert to HTML later."
  exit 1
end

title = ARGV[0]
date = Date.today
slug = title.downcase.gsub(/[^a-z0-9\s]/, '').gsub(/\s+/, '-')
filename = "#{date}-#{slug}.md"

# Create the post file
File.open(filename, 'w') do |file|
  file.puts "---"
  file.puts "title: \"#{title}\""
  file.puts "date: #{date.strftime('%B %d, %Y')}"
  file.puts "math: true"
  file.puts "---"
  file.puts ""
  file.puts "Write your blog post content here in markdown format."
  file.puts ""
  file.puts "You can use LaTeX math like this: $E = mc^2$"
  file.puts ""
  file.puts "For display math:"
  file.puts "$$\\int_{-\\infty}^{\\infty} e^{-x^2} dx = \\sqrt{\\pi}$$"
  file.puts ""
  file.puts "## Headers"
  file.puts ""
  file.puts "Use `##` for sections, `###` for subsections."
  file.puts ""
  file.puts "**Bold text** and *italic text* work as expected."
  file.puts ""
  file.puts "[Links work like this](https://example.com)"
end

puts "Created new markdown post: #{filename}"
puts ""
puts "Next steps:"
puts "1. Edit #{filename} with your content"
puts "2. Convert to HTML: python3 markdown_to_blog.py #{filename} --update-index"
puts "3. Your blog will be updated automatically!" 