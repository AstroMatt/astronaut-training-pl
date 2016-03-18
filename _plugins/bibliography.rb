module Jekyll
  module Tags
      class Bibliography < Liquid::Tag

        def initialize(tag_name, title, tokens)
          @title = title
          super
        end

        def clean(text)
            text.strip().gsub(/"/, '').gsub(/'/, '')
        end

        def find(context)
            Jekyll::logger::debug("Looking for '#{@title}'")
            bibliography = context.registers[:site].data['bibliography']

            index = bibliography.each_index.select{ |i|
                entry = clean(bibliography[i]['title'])
                title = clean(@title)
                Jekyll::logger::debug("Compare: '#{entry}' vs. '#{title}' == #{entry == title}")
                entry == title
            }

            if index.empty?
                raise IndexError, "Bibliography entry not found for title: '#{@title}'"
            end

            return index[0] + 1
        end

        def render(context)
            if "#{context['title']}"
                @title = "#{context['title']}"
            end

            index = find(context)
            return "[#{index}]"
        end
      end
  end
end

Liquid::Template.register_tag('bibliography', Jekyll::Tags::Bibliography)
