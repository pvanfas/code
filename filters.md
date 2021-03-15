---


---




  
  
  <title>filters</title>
  


  <div class="stackedit__left">
    <div class="stackedit__toc">
</div></div><ul>
<li><a href="#built-in-template-tags-and-filters">Built-in template tags and filters</a>
<ul>
<li><a href="#built-in-tag-reference">Built-in tag reference</a></li>
<li><a href="#built-in-filter-reference">Built-in filter reference</a></li>
</ul>
</li>
</ul>
<pre><code>&lt;/div&gt;
</code></pre>
  
  <div class="stackedit__right">
    <div class="stackedit__html">
      <h1 id="built-in-template-tags-and-filters">Built-in template tags and filters</h1>
<p>This document describes Django’s built-in template tags and filters. It is recommended that you use the  <a href="https://docs.djangoproject.com/en/3.1/ref/contrib/admin/admindocs/">automatic documentation</a>, if available, as this will also include documentation for any custom tags or filters installed.</p>
<h2 id="built-in-tag-reference">Built-in tag reference</h2>
<h3 id="autoescape"><code>autoescape</code></h3>
<p>Controls the current auto-escaping behavior. This tag takes either  <code>on</code>  or  <code>off</code>  as an argument and that determines whether auto-escaping is in effect inside the block. The block is closed with an  <code>endautoescape</code>  ending tag.</p>
<p>When auto-escaping is in effect, all variable content has HTML escaping applied to it before placing the result into the output (but after any filters have been applied). This is equivalent to manually applying the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-escape"><code>escape</code></a>  filter to each variable.</p>
<p>The only exceptions are variables that are already marked as “safe” from escaping, either by the code that populated the variable, or because it has had the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-safe"><code>safe</code></a>  or  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-escape"><code>escape</code></a>  filters applied.</p>
<p>Sample usage:</p>
<pre><code>{% autoescape on %}
    {{ body }}
{% endautoescape %}
</code></pre>
<hr>
<h3 id="comment"><code>comment</code></h3>
<p>Ignores everything between  <code>{% comment %}</code>  and  <code>{% endcomment %}</code>. An optional note may be inserted in the first tag. For example, this is useful when commenting out code for documenting why the code was disabled.</p>
<p>Sample usage:</p>
<pre><code>&lt;p&gt;Rendered text with {{ pub_date|date:"c" }}&lt;/p&gt;
{% comment "Optional note" %}
    &lt;p&gt;Commented out text with {{ create_date|date:"c" }}&lt;/p&gt;
{% endcomment %}
</code></pre>
<p><code>comment</code>  tags cannot be nested.</p>
<hr>
<h3 id="cycle"><code>cycle</code></h3>
<p>Produces one of its arguments each time this tag is encountered. The first argument is produced on the first encounter, the second argument on the second encounter, and so forth. Once all arguments are exhausted, the tag cycles to the first argument and produces it again.</p>
<p>This tag is particularly useful in a loop:</p>
<pre><code>{% for o in some_list %}
    &lt;tr class="{% cycle 'row1' 'row2' %}"&gt;
        ...
    &lt;/tr&gt;
{% endfor %}
</code></pre>
<p>The first iteration produces HTML that refers to class  <code>row1</code>, the second to  <code>row2</code>, the third to  <code>row1</code>  again, and so on for each iteration of the loop.</p>
<p>You can use variables, too. For example, if you have two template variables,  <code>rowvalue1</code>  and  <code>rowvalue2</code>, you can alternate between their values like this:</p>
<pre><code>{% for o in some_list %}
    &lt;tr class="{% cycle rowvalue1 rowvalue2 %}"&gt;
        ...
    &lt;/tr&gt;
{% endfor %}
</code></pre>
<p>Variables included in the cycle will be escaped. You can disable auto-escaping with:</p>
<pre><code>{% for o in some_list %}
    &lt;tr class="{% autoescape off %}{% cycle rowvalue1 rowvalue2 %}{% endautoescape %}"&gt;
        ...
    &lt;/tr&gt;
{% endfor %}
</code></pre>
<p>You can mix variables and strings:</p>
<pre><code>{% for o in some_list %}
    &lt;tr class="{% cycle 'row1' rowvalue2 'row3' %}"&gt;
        ...
    &lt;/tr&gt;
{% endfor %}
</code></pre>
<p>In some cases you might want to refer to the current value of a cycle without advancing to the next value. To do this, give the  <code>{% cycle %}</code>  tag a name, using “as”, like this:</p>
<pre><code>{% cycle 'row1' 'row2' as rowcolors %}
</code></pre>
<p>From then on, you can insert the current value of the cycle wherever you’d like in your template by referencing the cycle name as a context variable. If you want to move the cycle to the next value independently of the original  <code>cycle</code>  tag, you can use another  <code>cycle</code>  tag and specify the name of the variable. So, the following template:</p>
<pre><code>&lt;tr&gt;
    &lt;td class="{% cycle 'row1' 'row2' as rowcolors %}"&gt;...&lt;/td&gt;
    &lt;td class="{{ rowcolors }}"&gt;...&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
    &lt;td class="{% cycle rowcolors %}"&gt;...&lt;/td&gt;
    &lt;td class="{{ rowcolors }}"&gt;...&lt;/td&gt;
&lt;/tr&gt;
</code></pre>
<p>would output:</p>
<pre><code>&lt;tr&gt;
    &lt;td class="row1"&gt;...&lt;/td&gt;
    &lt;td class="row1"&gt;...&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
    &lt;td class="row2"&gt;...&lt;/td&gt;
    &lt;td class="row2"&gt;...&lt;/td&gt;
&lt;/tr&gt;
</code></pre>
<p>You can use any number of values in a  <code>cycle</code>  tag, separated by spaces. Values enclosed in single quotes (<code>'</code>) or double quotes (<code>"</code>) are treated as string literals, while values without quotes are treated as template variables.</p>
<p>By default, when you use the  <code>as</code>  keyword with the cycle tag, the usage of  <code>{% cycle %}</code>  that initiates the cycle will itself produce the first value in the cycle. This could be a problem if you want to use the value in a nested loop or an included template. If you only want to declare the cycle but not produce the first value, you can add a  <code>silent</code>  keyword as the last keyword in the tag. For example:</p>
<pre><code>{% for obj in some_list %}
    {% cycle 'row1' 'row2' as rowcolors silent %}
    &lt;tr class="{{ rowcolors }}"&gt;{% include "subtemplate.html" %}&lt;/tr&gt;
{% endfor %}
</code></pre>
<p>This will output a list of  <code>&lt;tr&gt;</code>  elements with  <code>class</code>  alternating between  <code>row1</code>  and  <code>row2</code>. The subtemplate will have access to  <code>rowcolors</code>  in its context and the value will match the class of the  <code>&lt;tr&gt;</code>  that encloses it. If the  <code>silent</code>  keyword were to be omitted,  <code>row1</code>  and  <code>row2</code>  would be emitted as normal text, outside the  <code>&lt;tr&gt;</code>  element.</p>
<p>When the silent keyword is used on a cycle definition, the silence automatically applies to all subsequent uses of that specific cycle tag. The following template would output  <em>nothing</em>, even though the second call to  <code>{% cycle %}</code>  doesn’t specify  <code>silent</code>:</p>
<pre><code>{% cycle 'row1' 'row2' as rowcolors silent %}
{% cycle rowcolors %}
</code></pre>
<p>You can use the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-resetcycle"><code>resetcycle</code></a>  tag to make a  <code>{% cycle %}</code>  tag restart from its first value when it’s next encountered.</p>
<hr>
<h3 id="filter"><code>filter</code></h3>
<p>Filters the contents of the block through one or more filters. Multiple filters can be specified with pipes and filters can have arguments, just as in variable syntax.</p>
<p>Note that the block includes  <em>all</em>  the text between the  <code>filter</code>  and  <code>endfilter</code>  tags.</p>
<p>Sample usage:</p>
<pre><code>{% filter force_escape|lower %}
    This text will be HTML-escaped, and will appear in all lowercase.
{% endfilter %}
</code></pre>
<blockquote>
<p><em>Note</em><br>
<em>The <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-escape"><code>escape</code></a> and <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-safe"><code>safe</code></a> filters are not acceptable arguments. Instead, use the <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-autoescape"><code>autoescape</code></a> tag to manage autoescaping for blocks of template code.</em></p>
</blockquote>
<hr>
<h3 id="firstof"><code>firstof</code></h3>
<p>Outputs the first argument variable that is not “false” (i.e. exists, is not empty, is not a false boolean value, and is not a zero numeric value). Outputs nothing if all the passed variables are “false”.</p>
<p>Sample usage:</p>
<pre><code>{% firstof var1 var2 var3 %}
</code></pre>
<p>This is equivalent to:</p>
<pre><code>{% if var1 %}
    {{ var1 }}
{% elif var2 %}
    {{ var2 }}
{% elif var3 %}
    {{ var3 }}
{% endif %}
</code></pre>
<p>You can also use a literal string as a fallback value in case all passed variables are False:</p>
<pre><code>{% firstof var1 var2 var3 "fallback value" %}
</code></pre>
<p>This tag auto-escapes variable values. You can disable auto-escaping with:</p>
<pre><code>{% autoescape off %}
    {% firstof var1 var2 var3 "&lt;strong&gt;fallback value&lt;/strong&gt;" %}
{% endautoescape %}
</code></pre>
<p>Or if only some variables should be escaped, you can use:</p>
<pre><code>{% firstof var1 var2|safe var3 "&lt;strong&gt;fallback value&lt;/strong&gt;"|safe %}
</code></pre>
<p>You can use the syntax  <code>{% firstof var1 var2 var3 as value %}</code>  to store the output inside a variable.</p>
<hr>
<h3 id="for"><code>for</code></h3>
<p>Loops over each item in an array, making the item available in a context variable. For example, to display a list of athletes provided in  <code>athlete_list</code>:</p>
<pre><code>&lt;ul&gt;
{% for athlete in athlete_list %}
    &lt;li&gt;{{ athlete.name }}&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
</code></pre>
<p>You can loop over a list in reverse by using  <code>{% for obj in list reversed %}</code>.</p>
<p>If you need to loop over a list of lists, you can unpack the values in each sublist into individual variables. For example, if your context contains a list of (x,y) coordinates called  <code>points</code>, you could use the following to output the list of points:</p>
<pre><code>{% for x, y in points %}
    There is a point at {{ x }},{{ y }}
{% endfor %}
</code></pre>
<p>This can also be useful if you need to access the items in a dictionary. For example, if your context contained a dictionary  <code>data</code>, the following would display the keys and values of the dictionary:</p>
<pre><code>{% for key, value in data.items %}
    {{ key }}: {{ value }}
{% endfor %}
</code></pre>
<p>Keep in mind that for the dot operator, dictionary key lookup takes precedence over method lookup. Therefore if the  <code>data</code>  dictionary contains a key named  <code>'items'</code>,  <code>data.items</code>  will return  <code>data['items']</code>  instead of  <code>data.items()</code>. Avoid adding keys that are named like dictionary methods if you want to use those methods in a template (<code>items</code>,  <code>values</code>,  <code>keys</code>, etc.). Read more about the lookup order of the dot operator in the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/language/#template-variables">documentation of template variables</a>.</p>
<p>The for loop sets a number of variables available within the loop:</p>
</div></div><table>
<thead>
<tr>
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>forloop.counter</code></td>
<td>The current iteration of the loop (1-indexed)</td>
</tr>
<tr>
<td><code>forloop.revcounter</code></td>
<td>The number of iterations from the end of the loop (1-indexed)</td>
</tr>
<tr>
<td><code>forloop.first</code></td>
<td>True if this is the first time through the loop</td>
</tr>
<tr>
<td><code>forloop.parentloop</code></td>
<td>For nested loops, this is the loop surrounding the current one</td>
</tr>
</tbody>
</table><hr>
<h3 id="for--…--empty"><code>for</code>  …  <code>empty</code></h3>
<p>The  <code>for</code>  tag can take an optional  <code>{% empty %}</code>  clause whose text is displayed if the given array is empty or could not be found:</p>
<pre><code>&lt;ul&gt;
{% for athlete in athlete_list %}
    &lt;li&gt;{{ athlete.name }}&lt;/li&gt;
{% empty %}
    &lt;li&gt;Sorry, no athletes in this list.&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
</code></pre>
<p>The above is equivalent to – but shorter, cleaner, and possibly faster than – the following:</p>
<pre><code>&lt;ul&gt;
  {% if athlete_list %}
    {% for athlete in athlete_list %}
      &lt;li&gt;{{ athlete.name }}&lt;/li&gt;
    {% endfor %}
  {% else %}
    &lt;li&gt;Sorry, no athletes in this list.&lt;/li&gt;
  {% endif %}
&lt;/ul&gt;
</code></pre>
<hr>
<h3 id="if"><code>if</code></h3>
<p>The  <code>{% if %}</code>  tag evaluates a variable, and if that variable is “true” (i.e. exists, is not empty, and is not a false boolean value) the contents of the block are output:</p>
<pre><code>{% if athlete_list %}
    Number of athletes: {{ athlete_list|length }}
{% elif athlete_in_locker_room_list %}
    Athletes should be out of the locker room soon!
{% else %}
    No athletes.
{% endif %}
</code></pre>
<p>In the above, if  <code>athlete_list</code>  is not empty, the number of athletes will be displayed by the  <code>{{ athlete_list|length }}</code>  variable.</p>
<p>As you can see, the  <code>if</code>  tag may take one or several  <code>{% elif %}</code>  clauses, as well as an  <code>{% else %}</code>  clause that will be displayed if all previous conditions fail. These clauses are optional.</p>
<hr>
<h4 id="boolean-operators">Boolean operators</h4>
<p><a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-if"><code>if</code></a>  tags may use  <code>and</code>,  <code>or</code>  or  <code>not</code>  to test a number of variables or to negate a given variable:</p>
<pre><code>{% if athlete_list and coach_list %}
    Both athletes and coaches are available.
{% endif %}
</code></pre><p>{% if not athlete_list %}<br>
There are no athletes.<br>
{% endif %}</p>
<p>{% if athlete_list or coach_list %}<br>
There are some athletes or some coaches.<br>
{% endif %}</p>
<p>{% if not athlete_list or coach_list %}<br>
There are no athletes or there are some coaches.<br>
{% endif %}</p>
<p>{% if athlete_list and not coach_list %}<br>
There are some athletes and absolutely no coaches.<br>
{% endif %}<br>
</p>
<p>Use of both  <code>and</code>  and  <code>or</code>  clauses within the same tag is allowed, with  <code>and</code>  having higher precedence than  <code>or</code>  e.g.:</p>
<pre><code>{% if athlete_list and coach_list or cheerleader_list %}
</code></pre>
<p>will be interpreted like:</p>
<pre><code>if (athlete_list and coach_list) or cheerleader_list
</code></pre>
<p>Use of actual parentheses in the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-if"><code>if</code></a>  tag is invalid syntax. If you need them to indicate precedence, you should use nested  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-if"><code>if</code></a>  tags.</p>
<p><a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-if"><code>if</code></a>  tags may also use the operators  <code>==</code>,  <code>!=</code>,  <code>&lt;</code>,  <code>&gt;</code>,  <code>&lt;=</code>,  <code>&gt;=</code>,  <code>in</code>,  <code>not in</code>,  <code>is</code>, and  <code>is not</code>  which work as follows:</p>
<h5 id="operator"><code>==</code>  operator</h5>
<p>Equality. Example:</p>
<pre><code>{% if somevar == "x" %}
  This appears if variable somevar equals the string "x"
{% endif %}
</code></pre>
<h5 id="operator-1"><code>!=</code>  operator</h5>
<p>Inequality. Example:</p>
<pre><code>{% if somevar != "x" %}
  This appears if variable somevar does not equal the string "x",
  or if somevar is not found in the context
{% endif %}
</code></pre>
<h5 id="operator-2"><code>&lt;</code>  operator</h5>
<p>Less than. Example:</p>
<pre><code>{% if somevar &lt; 100 %}
  This appears if variable somevar is less than 100.
{% endif %}
</code></pre>
<h5 id="operator-3"><code>&gt;</code>  operator</h5>
<p>Greater than. Example:</p>
<pre><code>{% if somevar &gt; 0 %}
  This appears if variable somevar is greater than 0.
{% endif %}
</code></pre>
<h5 id="operator-4"><code>&lt;=</code>  operator</h5>
<p>Less than or equal to. Example:</p>
<pre><code>{% if somevar &lt;= 100 %}
  This appears if variable somevar is less than 100 or equal to 100.
{% endif %}
</code></pre>
<h5 id="operator-5"><code>&gt;=</code>  operator</h5>
<p>Greater than or equal to. Example:</p>
<pre><code>{% if somevar &gt;= 1 %}
  This appears if variable somevar is greater than 1 or equal to 1.
{% endif %}
</code></pre>
<h5 id="in--operator"><code>in</code>  operator</h5>
<p>Contained within. This operator is supported by many Python containers to test whether the given value is in the container. The following are some examples of how  <code>x in y</code>  will be interpreted:</p>
<pre><code>{% if "bc" in "abcdef" %}
  This appears since "bc" is a substring of "abcdef"
{% endif %}
</code></pre><p>{% if “hello” in greetings %}<br>
If greetings is a list or set, one element of which is the string<br>
“hello”, this will appear.<br>
{% endif %}</p>
<p>{% if user in users %}<br>
If users is a QuerySet, this will appear if user is an<br>
instance that belongs to the QuerySet.<br>
{% endif %}<br>
</p>
<h5 id="not-in--operator"><code>not in</code>  operator</h5>
<p>Not contained within. This is the negation of the  <code>in</code>  operator.</p>
<h5 id="is--operator"><code>is</code>  operator</h5>
<p>Object identity. Tests if two values are the same object. Example:</p>
<pre><code>{% if somevar is True %}
  This appears if and only if somevar is True.
{% endif %}
</code></pre><p>{% if somevar is None %}<br>
This appears if somevar is None, or if somevar is not found in the context.<br>
{% endif %}<br>
</p>
<h5 id="is-not--operator"><code>is not</code>  operator</h5>
<p>Negated object identity. Tests if two values are not the same object. This is the negation of the  <code>is</code>  operator. Example:</p>
<pre><code>{% if somevar is not True %}
  This appears if somevar is not True, or if somevar is not found in the
  context.
{% endif %}
</code></pre><p>{% if somevar is not None %}<br>
This appears if and only if somevar is not None.<br>
{% endif %}<br>
</p>
<hr>
<h4 id="filters">Filters</h4>
<p>You can also use filters in the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-if"><code>if</code></a>  expression. For example:</p>
<pre><code>{% if messages|length &gt;= 100 %}
   You have lots of messages today!
{% endif %}
</code></pre>
<h4 id="complex-expressions-headline">Complex expressions headline")</h4>
<p>All of the above can be combined to form complex expressions. For such expressions, it can be important to know how the operators are grouped when the expression is evaluated - that is, the precedence rules. The precedence of the operators, from lowest to highest, is as follows:</p>
<ul>
<li><code>or</code></li>
<li><code>and</code></li>
<li><code>not</code></li>
<li><code>in</code></li>
<li><code>==</code>,  <code>!=</code>,  <code>&lt;</code>,  <code>&gt;</code>,  <code>&lt;=</code>,  <code>&gt;=</code></li>
</ul>
<p>(This follows Python exactly). So, for example, the following complex  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-if"><code>if</code></a>  tag:</p>
<p>{% if a == b or c == d and e %}</p>
<p>…will be interpreted as:</p>
<p>(a == b) or ((c == d) and e)</p>
<p>If you need different precedence, you will need to use nested  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-if"><code>if</code></a>  tags. Sometimes that is better for clarity anyway, for the sake of those who do not know the precedence rules.</p>
<p>The comparison operators cannot be ‘chained’ like in Python or in mathematical notation. For example, instead of using:</p>
<p>{% if a &gt; b &gt; c %}  (WRONG)</p>
<p>you should use:</p>
<p>{% if a &gt; b and b &gt; c %}</p>
<h3 id="include"><code>include</code></h3>
<p>Loads a template and renders it with the current context. This is a way of “including” other templates within a template.</p>
<p>This example includes the contents of the template  <code>"foo/bar.html"</code>:</p>
<pre><code>{% include "foo/bar.html" %}
</code></pre>
<p>This example includes the contents of the template whose name is contained in the variable  <code>template_name</code>:</p>
<pre><code>{% include template_name %}
</code></pre>
<p>You can pass additional context to the template using keyword arguments:</p>
<pre><code>{% include "name_snippet.html" with person="Jane" greeting="Hello" %}
</code></pre>
<p>If you want to render the context only with the variables provided (or even no variables at all), use the  <code>only</code>  option. No other variables are available to the included template:</p>
<pre><code>{% include "name_snippet.html" with greeting="Hi" only %}
</code></pre>
<hr>
<h3 id="lorem"><code>lorem</code></h3>
<p>Displays random “lorem ipsum” Latin text. This is useful for providing sample data in templates.</p>
<p>Usage:</p>
<pre><code>{% lorem [count] [method] [random] %}
</code></pre>
<p>Examples</p>
<ul>
<li><code>{% lorem %}</code>  will output the common “lorem ipsum” paragraph.</li>
<li><code>{% lorem 3 p %}</code>  will output the common “lorem ipsum” paragraph and two random paragraphs each wrapped in HTML  <code>&lt;p&gt;</code>  tags.</li>
<li><code>{% lorem 2 w random %}</code>  will output two random Latin words.</li>
</ul>
<hr>
<h3 id="regroup"><code>regroup</code></h3>
<p>Regroups a list of alike objects by a common attribute.</p>
<p>This complex tag is best illustrated by way of an example: say that  <code>cities</code>  is a list of cities represented by dictionaries containing  <code>"name"</code>,  <code>"population"</code>, and  <code>"country"</code>  keys:</p>
<pre><code>cities = [
    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
]
</code></pre>
<p>…and you’d like to display a hierarchical list that is ordered by country, like this:</p>
<pre><code>-   India
    -   Mumbai: 19,000,000
    -   Calcutta: 15,000,000
-   USA
    -   New York: 20,000,000
    -   Chicago: 7,000,000
-   Japan
    -   Tokyo: 33,000,000
</code></pre>
<p>You can use the  <code>{% regroup %}</code>  tag to group the list of cities by country. The following snippet of template code would accomplish this:</p>
<pre><code>{% regroup cities by country as country_list %}
</code></pre><p>&lt;ul&gt;<br>
{% for country in country_list %}<br>
&lt;li&gt;{{ country.grouper }}<br>
&lt;ul&gt;<br>
{% for city in country.list %}<br>
&lt;li&gt;{{ <a href="http://city.name">city.name</a> }}: {{ city.population }}&lt;/li&gt;<br>
{% endfor %}<br>
&lt;/ul&gt;<br>
&lt;/li&gt;<br>
{% endfor %}<br>
&lt;/ul&gt;<br>
</p>
<p>Let’s walk through this example.  <code>{% regroup %}</code>  takes three arguments: the list you want to regroup, the attribute to group by, and the name of the resulting list. Here, we’re regrouping the  <code>cities</code>  list by the  <code>country</code>  attribute and calling the result  <code>country_list</code>.</p>
<p><code>{% regroup %}</code>  produces a list (in this case,  <code>country_list</code>) of  <strong>group objects</strong>. Group objects are instances of  <a href="https://docs.python.org/3/library/collections.html#collections.namedtuple" title="(in Python v3.9)"><code>namedtuple()</code></a>  with two fields:</p>
<ul>
<li><code>grouper</code>  – the item that was grouped by (e.g., the string “India” or “Japan”).</li>
<li><code>list</code>  – a list of all items in this group (e.g., a list of all cities with country=’India’).</li>
</ul>
<p>Because  <code>{% regroup %}</code>  produces  <a href="https://docs.python.org/3/library/collections.html#collections.namedtuple" title="(in Python v3.9)"><code>namedtuple()</code></a>  objects, you can also write the previous example as:</p>
<p>{% regroup cities by country as country_list %}</p>
<pre><code>&lt;ul&gt;
{% for country, local_cities in country_list %}
    &lt;li&gt;{{ country }}
    &lt;ul&gt;
        {% for city in local_cities %}
          &lt;li&gt;{{ city.name }}: {{ city.population }}&lt;/li&gt;
        {% endfor %}
    &lt;/ul&gt;
    &lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
</code></pre>
<p>Note that  <code>{% regroup %}</code>  does not order its input! Our example relies on the fact that the  <code>cities</code>  list was ordered by  <code>country</code>  in the first place. If the  <code>cities</code>  list did  <em>not</em>  order its members by  <code>country</code>, the regrouping would naively display more than one group for a single country. For example, say the  <code>cities</code>  list was set to this (note that the countries are not grouped together):</p>
<pre><code>cities = [
    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
]
</code></pre>
<p>With this input for  <code>cities</code>, the example  <code>{% regroup %}</code>  template code above would result in the following output:</p>
<pre><code>-   India
    -   Mumbai: 19,000,000
-   USA
    -   New York: 20,000,000
-   India
    -   Calcutta: 15,000,000
-   USA
    -   Chicago: 7,000,000
-   Japan
    -   Tokyo: 33,000,000
</code></pre>
<p>The easiest solution to this gotcha is to make sure in your view code that the data is ordered according to how you want to display it.</p>
<p>Another solution is to sort the data in the template using the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-dictsort"><code>dictsort</code></a>  filter, if your data is in a list of dictionaries:</p>
<pre><code>{% regroup cities|dictsort:"country" by country as country_list %}
</code></pre>
<hr>
<h3 id="resetcycle"><code>resetcycle</code></h3>
<p>Resets a previous  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#cycle">cycle</a>  so that it restarts from its first item at its next encounter. Without arguments,  <code>{% resetcycle %}</code>  will reset the last  <code>{% cycle %}</code>  defined in the template.</p>
<p>Example usage:</p>
<pre><code>{% for coach in coach_list %}
    &lt;h1&gt;{{ coach.name }}&lt;/h1&gt;
    {% for athlete in coach.athlete_set.all %}
        &lt;p class="{% cycle 'odd' 'even' %}"&gt;{{ athlete.name }}&lt;/p&gt;
    {% endfor %}
    {% resetcycle %}
{% endfor %}
</code></pre>
<p>This example would return this HTML:</p>
<pre><code>&lt;h1&gt;José Mourinho&lt;/h1&gt;
&lt;p class="odd"&gt;Thibaut Courtois&lt;/p&gt;
&lt;p class="even"&gt;John Terry&lt;/p&gt;
&lt;p class="odd"&gt;Eden Hazard&lt;/p&gt;
</code></pre><p>&lt;h1&gt;Carlo Ancelotti&lt;/h1&gt;<br>
&lt;p class=“odd”&gt;Manuel Neuer&lt;/p&gt;<br>
&lt;p class=“even”&gt;Thomas Müller&lt;/p&gt;<br>
</p>
<p>Notice how the first block ends with  <code>class="odd"</code>  and the new one starts with  <code>class="odd"</code>. Without the  <code>{% resetcycle %}</code>  tag, the second block would start with  <code>class="even"</code>.</p>
<p>You can also reset named cycle tags:</p>
<pre><code>{% for item in list %}
    &lt;p class="{% cycle 'odd' 'even' as stripe %}  {% cycle 'major' 'minor' 'minor' 'minor' 'minor' as tick %}"&gt;
        {{ item.data }}
    &lt;/p&gt;
    {% ifchanged item.category %}
        &lt;h1&gt;{{ item.category }}&lt;/h1&gt;
        {% if not forloop.first %}{% resetcycle tick %}{% endif %}
    {% endifchanged %}
{% endfor %}
</code></pre>
<p>In this example, we have both the alternating odd/even rows and a “major” row every fifth row. Only the five-row cycle is reset when a category changes.</p>
<hr>
<h3 id="spaceless"><code>spaceless</code></h3>
<p>Removes whitespace between HTML tags. This includes tab characters and newlines.</p>
<p>Example usage:</p>
<pre><code>{% spaceless %}
    &lt;p&gt;
        &lt;a href="foo/"&gt;Foo&lt;/a&gt;
    &lt;/p&gt;
{% endspaceless %}
</code></pre>
<p>This example would return this HTML:</p>
<pre><code>&lt;p&gt;&lt;a href="foo/"&gt;Foo&lt;/a&gt;&lt;/p&gt;
</code></pre>
<hr>
<h3 id="widthratio"><code>widthratio</code></h3>
<p>For creating bar charts and such, this tag calculates the ratio of a given value to a maximum value, and then applies that ratio to a constant.</p>
<p>For example:</p>
<pre><code>&lt;img src="bar.png" alt="Bar"
     height="10" width="{% widthratio this_value max_value max_width %}"&gt;
</code></pre>
<p>If  <code>this_value</code>  is 175,  <code>max_value</code>  is 200, and  <code>max_width</code>  is 100, the image in the above example will be 88 pixels wide (because 175/200 = .875; .875 * 100 = 87.5 which is rounded up to 88).</p>
<p>In some cases you might want to capture the result of  <code>widthratio</code>  in a variable. It can be useful, for instance, in a  <a href="https://docs.djangoproject.com/en/3.1/topics/i18n/translation/#std:templatetag-blocktranslate"><code>blocktranslate</code></a>  like this:</p>
<pre><code>{% widthratio this_value max_value max_width as width %}
{% blocktranslate %}The width is: {{ width }}{% endblocktranslate %}
</code></pre>
<hr>
<h3 id="with"><code>with</code></h3>
<p>Caches a complex variable under a simpler name. This is useful when accessing an “expensive” method (e.g., one that hits the database) multiple times.</p>
<p>For example:</p>
<pre><code>{% with total=business.employees.count %}
    {{ total }} employee{{ total|pluralize }}
{% endwith %}
</code></pre>
<p>The populated variable (in the example above,  <code>total</code>) is only available between the  <code>{% with %}</code>  and  <code>{% endwith %}</code>  tags.</p>
<p>You can assign more than one context variable:</p>
<pre><code>{% with alpha=1 beta=2 %}
    ...
{% endwith %}
</code></pre>
<h2 id="built-in-filter-reference">Built-in filter reference</h2>
<h3 id="add"><code>add</code></h3>
<p>Adds the argument to the value.</p>
<p>For example:</p>
<pre><code>{{ value|add:"2" }}
</code></pre>
<p>If  <code>value</code>  is  <code>4</code>, then the output will be  <code>6</code>.</p>
<p>This filter will first try to coerce both values to integers. If this fails, it’ll attempt to add the values together anyway. This will work on some data types (strings, list, etc.) and fail on others. If it fails, the result will be an empty string.</p>
<p>For example, if we have:</p>
<pre><code>{{ first|add:second }}
</code></pre>
<p>and  <code>first</code>  is  <code>[1, 2, 3]</code>  and  <code>second</code>  is  <code>[4, 5, 6]</code>, then the output will be  <code>[1, 2, 3, 4, 5, 6]</code>.</p>
<p>Warning</p>
<p>Strings that can be coerced to integers will be  <strong>summed</strong>, not concatenated, as in the first example above.</p>
<h3 id="addslashes"><code>addslashes</code></h3>
<p>Adds slashes before quotes. Useful for escaping strings in CSV, for example.</p>
<p>For example:</p>
<pre><code>{{ value|addslashes }}
</code></pre>
<p>If  <code>value</code>  is  <code>"I'm using Django"</code>, the output will be  <code>"I\'m using Django"</code>.</p>
<h3 id="capfirst"><code>capfirst</code></h3>
<p>Capitalizes the first character of the value. If the first character is not a letter, this filter has no effect.</p>
<p>For example:</p>
<p>{{ value|capfirst }}</p>
<p>If  <code>value</code>  is  <code>"django"</code>, the output will be  <code>"Django"</code>.</p>
<hr>
<h3 id="cut"><code>cut</code></h3>
<p>Removes all values of arg from the given string.</p>
<p>For example:</p>
<pre><code>{{ value|cut:" " }}
</code></pre>
<p>If  <code>value</code>  is  <code>"String with spaces"</code>, the output will be  <code>"Stringwithspaces"</code>.</p>
<h3 id="default"><code>default</code></h3>
<p>If value evaluates to  <code>False</code>, uses the given default. Otherwise, uses the value.</p>
<p>For example:</p>
<pre><code>{{ value|default:"nothing" }}
</code></pre>
<p>If  <code>value</code>  is  <code>""</code>  (the empty string), the output will be  <code>nothing</code>.</p>
<h3 id="default_if_none"><code>default_if_none</code></h3>
<p>If (and only if) value is  <code>None</code>, uses the given default. Otherwise, uses the value.</p>
<p>Note that if an empty string is given, the default value will  <em>not</em>  be used. Use the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-default"><code>default</code></a>  filter if you want to fallback for empty strings.</p>
<p>For example:</p>
<p>{{ value|default_if_none:“nothing” }}</p>
<p>If  <code>value</code>  is  <code>None</code>, the output will be  <code>nothing</code>.</p>
<h3 id="dictsort"><code>dictsort</code></h3>
<p>Takes a list of dictionaries and returns that list sorted by the key given in the argument.</p>
<p>For example:</p>
<pre><code>{{ value|dictsort:"name" }}
</code></pre><p>If  <code>value</code>  is:</p>
<p>[<br>
{‘name’: ‘zed’, ‘age’: 19},<br>
{‘name’: ‘amy’, ‘age’: 22},<br>
{‘name’: ‘joe’, ‘age’: 31},<br>
]<br>
</p>
<p>then the output would be:</p>
<pre><code>[
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
    {'name': 'zed', 'age': 19},
]
</code></pre>
<p>You can also do more complicated things like:</p>
<pre><code>{% for book in books|dictsort:"author.age" %}
    * {{ book.title }} ({{ book.author.name }})
{% endfor %}
</code></pre><p>If  <code>books</code>  is:</p>
<p>[<br>
{‘title’: ‘1984’, ‘author’: {‘name’: ‘George’, ‘age’: 45}},<br>
{‘title’: ‘Timequake’, ‘author’: {‘name’: ‘Kurt’, ‘age’: 75}},<br>
{‘title’: ‘Alice’, ‘author’: {‘name’: ‘Lewis’, ‘age’: 33}},<br>
]<br>
</p>
<p>then the output would be:</p>
<pre><code>* Alice (Lewis)
* 1984 (George)
* Timequake (Kurt)
</code></pre>
<p><code>dictsort</code>  can also order a list of lists (or any other object implementing  <code>__getitem__()</code>) by elements at specified index. For example:</p>
<pre><code>{{ value|dictsort:0 }}
</code></pre><p>If  <code>value</code>  is:</p>
<p>[<br>
(‘a’, ‘42’),<br>
(‘c’, ‘string’),<br>
(‘b’, ‘foo’),<br>
]<br>
</p>
<p>then the output would be:</p>
<pre><code>[
    ('a', '42'),
    ('b', 'foo'),
    ('c', 'string'),
]
</code></pre>
<p>You must pass the index as an integer rather than a string. The following produce empty output:</p>
<pre><code>{{ values|dictsort:"0" }}
</code></pre>
<h3 id="dictsortreversed"><code>dictsortreversed</code></h3>
<p>Takes a list of dictionaries and returns that list sorted in reverse order by the key given in the argument. This works exactly the same as the above filter, but the returned value will be in reverse order.</p>
<h3 id="divisibleby"><code>divisibleby</code></h3>
<p>Returns  <code>True</code>  if the value is divisible by the argument.</p>
<p>For example:</p>
<pre><code>{{ value|divisibleby:"3" }}
</code></pre>
<p>If  <code>value</code>  is  <code>21</code>, the output would be  <code>True</code>.</p>
<h3 id="escape"><code>escape</code></h3>
<p>Escapes a string’s HTML. Specifically, it makes these replacements:</p>
<ul>
<li><code>&lt;</code>  is converted to  <code>&amp;lt;</code></li>
<li><code>&gt;</code>  is converted to  <code>&amp;gt;</code></li>
<li><code>'</code>  (single quote) is converted to  <code>&amp;#x27;</code></li>
<li><code>"</code>  (double quote) is converted to  <code>&amp;quot;</code></li>
<li><code>&amp;</code>  is converted to  <code>&amp;amp;</code></li>
</ul>
<p>Applying  <code>escape</code>  to a variable that would normally have auto-escaping applied to the result will only result in one round of escaping being done. So it is safe to use this function even in auto-escaping environments. If you want multiple escaping passes to be applied, use the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-force_escape"><code>force_escape</code></a>  filter.</p>
<p>For example, you can apply  <code>escape</code>  to fields when  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-autoescape"><code>autoescape</code></a>  is off:</p>
<pre><code>{% autoescape off %}
    {{ title|escape }}
{% endautoescape %}
</code></pre>
<h3 id="escapejs"><code>escapejs</code></h3>
<p>Escapes characters for use in JavaScript strings. This does  <em>not</em>  make the string safe for use in HTML or JavaScript template literals, but does protect you from syntax errors when using templates to generate JavaScript/JSON.</p>
<p>For example:</p>
<pre><code>{{ value|escapejs }}
</code></pre>
<p>If  <code>value</code>  is  <code>"testing\r\njavascript 'string\" &lt;b&gt;escaping&lt;/b&gt;"</code>, the output will be  <code>"testing\\u000D\\u000Ajavascript \\u0027string\\u0022 \\u003Cb\\u003Eescaping\\u003C/b\\u003E"</code>.</p>
<h3 id="filesizeformat"><code>filesizeformat</code></h3>
<p>Formats the value like a ‘human-readable’ file size (i.e.  <code>'13 KB'</code>,  <code>'4.1 MB'</code>,  <code>'102 bytes'</code>, etc.).</p>
<p>For example:</p>
<pre><code>{{ value|filesizeformat }}
</code></pre>
<p>If  <code>value</code>  is 123456789, the output would be  <code>117.7 MB</code>.</p>
<p>File sizes and SI units</p>
<p>Strictly speaking,  <code>filesizeformat</code>  does not conform to the International System of Units which recommends using KiB, MiB, GiB, etc. when byte sizes are calculated in powers of 1024 (which is the case here). Instead, Django uses traditional unit names (KB, MB, GB, etc.) corresponding to names that are more commonly used.</p>
<h3 id="first"><code>first</code></h3>
<p>Returns the first item in a list.</p>
<p>For example:</p>
<pre><code>{{ value|first }}
</code></pre>
<p>If  <code>value</code>  is the list  <code>['a', 'b', 'c']</code>, the output will be  <code>'a'</code>.</p>
<h3 id="floatformat"><code>floatformat</code></h3>
<p>When used without an argument, rounds a floating-point number to one decimal place – but only if there’s a decimal part to be displayed. For example:</p>
<table>
<thead>
<tr>
<th><code>value</code></th>
<th>Template</th>
<th>Output</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>34.23234</code></td>
<td><code>{{ value|floatformat }}</code></td>
<td><code>34.2</code></td>
</tr>
<tr>
<td><code>34.00000</code></td>
<td><code>{{ value|floatformat }}</code></td>
<td><code>34</code></td>
</tr>
<tr>
<td><code>34.26000</code></td>
<td><code>{{ value|floatformat }}</code></td>
<td><code>34.3</code></td>
</tr>
</tbody>
</table><p>If used with a numeric integer argument,  <code>floatformat</code>  rounds a number to that many decimal places. For example:</p>
<table>
<thead>
<tr>
<th><code>value</code></th>
<th>Template</th>
<th>Output</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>34.23234</code></td>
<td><code>{{ value|floatformat:3 }}</code></td>
<td><code>34.232</code></td>
</tr>
<tr>
<td><code>34.00000</code></td>
<td><code>{{ value|floatformat:3 }}</code></td>
<td><code>34.000</code></td>
</tr>
<tr>
<td><code>34.26000</code></td>
<td><code>{{ value|floatformat:3 }}</code></td>
<td><code>34.260</code></td>
</tr>
</tbody>
</table><p>Particularly useful is passing 0 (zero) as the argument which will round the float to the nearest integer.</p>
<table>
<thead>
<tr>
<th><code>value</code></th>
<th>Template</th>
<th>Output</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>34.23234</code></td>
<td><code>{{ value|floatformat:"0" }}</code></td>
<td><code>34</code></td>
</tr>
<tr>
<td><code>34.00000</code></td>
<td><code>{{ value|floatformat:"0" }}</code></td>
<td><code>34</code></td>
</tr>
<tr>
<td><code>39.56000</code></td>
<td><code>{{ value|floatformat:"0" }}</code></td>
<td><code>40</code></td>
</tr>
</tbody>
</table><p>If the argument passed to  <code>floatformat</code>  is negative, it will round a number to that many decimal places – but only if there’s a decimal part to be displayed. For example:</p>
<table>
<thead>
<tr>
<th><code>value</code></th>
<th>Template</th>
<th>Output</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>34.23234</code></td>
<td><code>{{ value|floatformat:"-3" }}</code></td>
<td><code>34.232</code></td>
</tr>
<tr>
<td><code>34.00000</code></td>
<td><code>{{ value|floatformat:"-3" }}</code></td>
<td><code>34</code></td>
</tr>
<tr>
<td><code>34.26000</code></td>
<td><code>{{ value|floatformat:"-3" }}</code></td>
<td><code>34.260</code></td>
</tr>
</tbody>
</table><p>Using  <code>floatformat</code>  with no argument is equivalent to using  <code>floatformat</code>  with an argument of  <code>-1</code>.</p>
<p>Changed in Django 3.1:</p>
<p>In older versions, a negative zero  <code>-0</code>  was returned for negative numbers which round to zero.</p>
<h3 id="force_escape"><code>force_escape</code></h3>
<p>Applies HTML escaping to a string (see the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-escape"><code>escape</code></a>  filter for details). This filter is applied  <em>immediately</em>  and returns a new, escaped string. This is useful in the rare cases where you need multiple escaping or want to apply other filters to the escaped results. Normally, you want to use the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-escape"><code>escape</code></a>  filter.</p>
<p>For example, if you want to catch the  <code>&lt;p&gt;</code>  HTML elements created by the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-linebreaks"><code>linebreaks</code></a>  filter:</p>
<pre><code>{% autoescape off %}
    {{ body|linebreaks|force_escape }}
{% endautoescape %}
</code></pre>
<h3 id="get_digit"><code>get_digit</code></h3>
<p>Given a whole number, returns the requested digit, where 1 is the right-most digit, 2 is the second-right-most digit, etc. Returns the original value for invalid input (if input or argument is not an integer, or if argument is less than 1). Otherwise, output is always an integer.</p>
<p>For example:</p>
<pre><code>{{ value|get_digit:"2" }}
</code></pre>
<p>If  <code>value</code>  is  <code>123456789</code>, the output will be  <code>8</code>.</p>
<h3 id="iriencode"><code>iriencode</code></h3>
<p>Converts an IRI (Internationalized Resource Identifier) to a string that is suitable for including in a URL. This is necessary if you’re trying to use strings containing non-ASCII characters in a URL.</p>
<p>It’s safe to use this filter on a string that has already gone through the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-urlencode"><code>urlencode</code></a>  filter.</p>
<p>For example:</p>
<pre><code>{{ value|iriencode }}
</code></pre>
<p>If  <code>value</code>  is  <code>"?test=1&amp;me=2"</code>, the output will be  <code>"?test=1&amp;amp;me=2"</code>.</p>
<h3 id="join"><code>join</code></h3>
<p>Joins a list with a string, like Python’s  <code>str.join(list)</code></p>
<p>For example:</p>
<pre><code>{{ value|join:" // " }}
</code></pre>
<p>If  <code>value</code>  is the list  <code>['a', 'b', 'c']</code>, the output will be the string  <code>"a // b // c"</code>.</p>
<h3 id="json_script"><code>json_script</code></h3>
<p>Safely outputs a Python object as JSON, wrapped in a  <code>&lt;script&gt;</code>  tag, ready for use with JavaScript.</p>
<p><strong>Argument:</strong>  HTML “id” of the  <code>&lt;script&gt;</code>  tag.</p>
<p>For example:</p>
<pre><code>{{ value|json_script:"hello-data" }}
</code></pre>
<p>If  <code>value</code>  is the dictionary  <code>{'hello': 'world'}</code>, the output will be:</p>
<pre><code>&lt;script id="hello-data" type="application/json"&gt;{"hello": "world"}&lt;/script&gt;
</code></pre>
<p>The resulting data can be accessed in JavaScript like this:</p>
<pre><code>const value = JSON.parse(document.getElementById('hello-data').textContent);
</code></pre>
<p>XSS attacks are mitigated by escaping the characters “&lt;”, “&gt;” and “&amp;”. For example if  <code>value</code>  is  <code>{'hello': 'world&lt;/script&gt;&amp;amp;'}</code>, the output is:</p>
<p>This is compatible with a strict Content Security Policy that prohibits in-page script execution. It also maintains a clean separation between passive data and executable code.</p>
<h3 id="last"><code>last</code></h3>
<p>Returns the last item in a list.</p>
<p>For example:</p>
<pre><code>{{ value|last }}
</code></pre>
<p>If  <code>value</code>  is the list  <code>['a', 'b', 'c', 'd']</code>, the output will be the string  <code>"d"</code>.</p>
<h3 id="length"><code>length</code></h3>
<p>Returns the length of the value. This works for both strings and lists.</p>
<p>For example:</p>
<pre><code>{{ value|length }}
</code></pre>
<p>If  <code>value</code>  is  <code>['a', 'b', 'c', 'd']</code>  or  <code>"abcd"</code>, the output will be  <code>4</code>.</p>
<p>The filter returns  <code>0</code>  for an undefined variable.</p>
<h3 id="length_is"><code>length_is</code></h3>
<p>Returns  <code>True</code>  if the value’s length is the argument, or  <code>False</code>  otherwise.</p>
<p>For example:</p>
<pre><code>{{ value|length_is:"4" }}
</code></pre>
<p>If  <code>value</code>  is  <code>['a', 'b', 'c', 'd']</code>  or  <code>"abcd"</code>, the output will be  <code>True</code>.</p>
<h3 id="linebreaks"><code>linebreaks</code></h3>
<p>Replaces line breaks in plain text with appropriate HTML; a single newline becomes an HTML line break (<code>&lt;br&gt;</code>) and a new line followed by a blank line becomes a paragraph break (<code>&lt;/p&gt;</code>).</p>
<p>For example:</p>
<pre><code>{{ value|linebreaks }}
</code></pre>
<p>If  <code>value</code>  is  <code>Joel\nis a slug</code>, the output will be  <code>&lt;p&gt;Joel&lt;br&gt;is a slug&lt;/p&gt;</code>.</p>
<h3 id="linebreaksbr"><code>linebreaksbr</code></h3>
<p>Converts all newlines in a piece of plain text to HTML line breaks (<code>&lt;br&gt;</code>).</p>
<p>For example:</p>
<pre><code>{{ value|linebreaksbr }}
</code></pre>
<p>If  <code>value</code>  is  <code>Joel\nis a slug</code>, the output will be  <code>Joel&lt;br&gt;is a slug</code>.</p>
<h3 id="linenumbers"><code>linenumbers</code></h3>
<p>Displays text with line numbers.</p>
<p>For example:</p>
<pre><code>{{ value|linenumbers }}
</code></pre>
<p>If  <code>value</code>  is:</p>
<pre><code>one
two
three
</code></pre>
<p>the output will be:</p>
<pre><code>1. one
2. two
3. three
</code></pre>
<h3 id="ljust"><code>ljust</code></h3>
<p>Left-aligns the value in a field of a given width.</p>
<p><strong>Argument:</strong>  field size</p>
<p>For example:</p>
<pre><code>"{{ value|ljust:"10" }}"
</code></pre>
<p>If  <code>value</code>  is  <code>Django</code>, the output will be  <code>"Django "</code>.</p>
<h3 id="lower"><code>lower</code></h3>
<p>Converts a string into all lowercase.</p>
<p>For example:</p>
<pre><code>{{ value|lower }}
</code></pre>
<p>If  <code>value</code>  is  <code>Totally LOVING this Album!</code>, the output will be  <code>totally loving this album!</code>.</p>
<h3 id="make_list"><code>make_list</code></h3>
<p>Returns the value turned into a list. For a string, it’s a list of characters. For an integer, the argument is cast to a string before creating a list.</p>
<p>For example:</p>
<pre><code>{{ value|make_list }}
</code></pre>
<p>If  <code>value</code>  is the string  <code>"Joel"</code>, the output would be the list  <code>['J', 'o', 'e', 'l']</code>. If  <code>value</code>  is  <code>123</code>, the output will be the list  <code>['1', '2', '3']</code>.</p>
<h3 id="phone2numeric"><code>phone2numeric</code></h3>
<p>Converts a phone number (possibly containing letters) to its numerical equivalent.</p>
<p>The input doesn’t have to be a valid phone number. This will happily convert any string.</p>
<p>For example:</p>
<p>{{ value|phone2numeric }}</p>
<p>If  <code>value</code>  is  <code>800-COLLECT</code>, the output will be  <code>800-2655328</code>.</p>
<h3 id="pluralize"><code>pluralize</code></h3>
<p>Returns a plural suffix if the value is not  <code>1</code>,  <code>'1'</code>, or an object of length 1. By default, this suffix is  <code>'s'</code>.</p>
<p>Example:</p>
<p>You have {{ num_messages }} message{{ num_messages|pluralize }}.</p>
<p>If  <code>num_messages</code>  is  <code>1</code>, the output will be  <code>You have 1 message.</code>  If  <code>num_messages</code>  is  <code>2</code>  the output will be  <code>You have 2 messages.</code></p>
<p>For words that require a suffix other than  <code>'s'</code>, you can provide an alternate suffix as a parameter to the filter.</p>
<p>Example:</p>
<p>You have {{ num_walruses }} walrus{{ num_walruses|pluralize:“es” }}.</p>
<p>For words that don’t pluralize by simple suffix, you can specify both a singular and plural suffix, separated by a comma.</p>
<p>Example:</p>
<p>You have {{ num_cherries }} cherr{{ num_cherries|pluralize:“y,ies” }}.</p>
<p>Note</p>
<p>Use  <a href="https://docs.djangoproject.com/en/3.1/topics/i18n/translation/#std:templatetag-blocktranslate"><code>blocktranslate</code></a>  to pluralize translated strings.</p>
<h3 id="random"><code>random</code></h3>
<p>Returns a random item from the given list.</p>
<p>For example:</p>
<pre><code>{{ value|random }}
</code></pre>
<p>If  <code>value</code>  is the list  <code>['a', 'b', 'c', 'd']</code>, the output could be  <code>"b"</code>.</p>
<h3 id="rjust"><code>rjust</code></h3>
<p>Right-aligns the value in a field of a given width.</p>
<p><strong>Argument:</strong>  field size</p>
<p>For example:</p>
<pre><code>"{{ value|rjust:"10" }}"
</code></pre>
<p>If  <code>value</code>  is  <code>Django</code>, the output will be  <code>" Django"</code>.</p>
<h3 id="safe"><code>safe</code></h3>
<p>Marks a string as not requiring further HTML escaping prior to output. When autoescaping is off, this filter has no effect.</p>
<p>Note</p>
<p>If you are chaining filters, a filter applied after  <code>safe</code>  can make the contents unsafe again. For example, the following code prints the variable as is, unescaped:</p>
<pre><code>{{ var|safe|escape }}
</code></pre>
<h3 id="safeseq"><code>safeseq</code></h3>
<p>Applies the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-safe"><code>safe</code></a>  filter to each element of a sequence. Useful in conjunction with other filters that operate on sequences, such as  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-join"><code>join</code></a>. For example:</p>
<pre><code>{{ some_list|safeseq|join:", " }}
</code></pre>
<p>You couldn’t use the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-safe"><code>safe</code></a>  filter directly in this case, as it would first convert the variable into a string, rather than working with the individual elements of the sequence.</p>
<h3 id="slice"><code>slice</code></h3>
<p>Returns a slice of the list.</p>
<p>Uses the same syntax as Python’s list slicing. See  <a href="https://www.diveinto.org/python3/native-datatypes.html#slicinglists">https://www.diveinto.org/python3/native-datatypes.html#slicinglists</a>  for an introduction.</p>
<p>Example:</p>
<pre><code>{{ some_list|slice:":2" }}
</code></pre>
<p>If  <code>some_list</code>  is  <code>['a', 'b', 'c']</code>, the output will be  <code>['a', 'b']</code>.</p>
<h3 id="slugify"><code>slugify</code></h3>
<p>Converts to ASCII. Converts spaces to hyphens. Removes characters that aren’t alphanumerics, underscores, or hyphens. Converts to lowercase. Also strips leading and trailing whitespace.</p>
<p>For example:</p>
<pre><code>{{ value|slugify }}
</code></pre>
<p>If  <code>value</code>  is  <code>"Joel is a slug"</code>, the output will be  <code>"joel-is-a-slug"</code>.</p>
<h3 id="stringformat"><code>stringformat</code></h3>
<p>Formats the variable according to the argument, a string formatting specifier. This specifier uses the  <a href="https://docs.python.org/3/library/stdtypes.html#old-string-formatting" title="(in Python v3.9)">printf-style String Formatting</a>  syntax, with the exception that the leading “%” is dropped.</p>
<p>For example:</p>
<pre><code>{{ value|stringformat:"E" }}
</code></pre>
<p>If  <code>value</code>  is  <code>10</code>, the output will be  <code>1.000000E+01</code>.</p>
<h3 id="striptags"><code>striptags</code></h3>
<p>Makes all possible efforts to strip all [X]HTML tags.</p>
<p>For example:</p>
<pre><code>{{ value|striptags }}
</code></pre>
<p>If  <code>value</code>  is  <code>"&lt;b&gt;Joel&lt;/b&gt; &lt;button&gt;is&lt;/button&gt; a &lt;span&gt;slug&lt;/span&gt;"</code>, the output will be  <code>"Joel is a slug"</code>.</p>
<p>No safety guarantee</p>
<p>Note that  <code>striptags</code>  doesn’t give any guarantee about its output being HTML safe, particularly with non valid HTML input. So  <strong>NEVER</strong>  apply the  <code>safe</code>  filter to a  <code>striptags</code>  output. If you are looking for something more robust, you can use the  <code>bleach</code>  Python library, notably its  <a href="https://bleach.readthedocs.io/en/latest/clean.html">clean</a>  method.</p>
<h3 id="time"><code>time</code></h3>
<p>Formats a time according to the given format.</p>
<p>Given format can be the predefined one  <a href="https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-TIME_FORMAT"><code>TIME_FORMAT</code></a>, or a custom format, same as the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-date"><code>date</code></a>  filter. Note that the predefined format is locale-dependent.</p>
<p>For example:</p>
<pre><code>{{ value|time:"H:i" }}
</code></pre>
<p>If  <code>value</code>  is equivalent to  <code>datetime.datetime.now()</code>, the output will be the string  <code>"01:23"</code>.</p>
<p>Note that you can backslash-escape a format string if you want to use the “raw” value. In this example, both “h” and “m” are backslash-escaped, because otherwise each is a format string that displays the hour and the month, respectively:</p>
<pre><code>{% value|time:"H\h i\m" %}
</code></pre>
<p>This would display as <code>“01h 23m”.</code></p>
<p>Another example:</p>
<p>Assuming that  <a href="https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-USE_L10N"><code>USE_L10N</code></a>  is  <code>True</code>  and  <a href="https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-LANGUAGE_CODE"><code>LANGUAGE_CODE</code></a>  is, for example,  <code>"de"</code>, then for:</p>
<pre><code>{{ value|time:"TIME_FORMAT" }}
</code></pre>
<p>the output will be the string  <code>"01:23"</code>  (The  <code>"TIME_FORMAT"</code>  format specifier for the  <code>de</code>  locale as shipped with Django is  <code>"H:i"</code>).</p>
<p>The  <code>time</code>  filter will only accept parameters in the format string that relate to the time of day, not the date. If you need to format a  <code>date</code>  value, use the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-date"><code>date</code></a>  filter instead (or along with  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-time"><code>time</code></a>  if you need to render a full  <a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.9)"><code>datetime</code></a>  value).</p>
<p>There is one exception the above rule: When passed a  <code>datetime</code>  value with attached timezone information (a  <a href="https://docs.djangoproject.com/en/3.1/topics/i18n/timezones/#naive-vs-aware-datetimes">time-zone-aware</a>  <code>datetime</code>  instance) the  <code>time</code>  filter will accept the timezone-related  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#date-and-time-formatting-specifiers">format specifiers</a>  <code>'e'</code>,  <code>'O'</code>  ,  <code>'T'</code>  and  <code>'Z'</code>.</p>
<p>When used without a format string, the  <code>TIME_FORMAT</code>  format specifier is used:</p>
<pre><code>{{ value|time }}
</code></pre>
<p>is the same as:</p>
<pre><code>{{ value|time:"TIME_FORMAT" }}
</code></pre>
<h3 id="timesince"><code>timesince</code></h3>
<p>Formats a date as the time since that date (e.g., “4 days, 6 hours”).</p>
<p>Takes an optional argument that is a variable containing the date to use as the comparison point (without the argument, the comparison point is  <em>now</em>). For example, if  <code>blog_date</code>  is a date instance representing midnight on 1 June 2006, and  <code>comment_date</code>  is a date instance for 08:00 on 1 June 2006, then the following would return “8 hours”:</p>
<pre><code>{{ blog_date|timesince:comment_date }}
</code></pre>
<p>Comparing offset-naive and offset-aware datetimes will return an empty string.</p>
<p>Minutes is the smallest unit used, and “0 minutes” will be returned for any date that is in the future relative to the comparison point.</p>
<h3 id="timeuntil"><code>timeuntil</code></h3>
<p>Similar to  <code>timesince</code>, except that it measures the time from now until the given date or datetime. For example, if today is 1 June 2006 and  <code>conference_date</code>  is a date instance holding 29 June 2006, then  <code>{{ conference_date|timeuntil }}</code>  will return “4 weeks”.</p>
<p>Takes an optional argument that is a variable containing the date to use as the comparison point (instead of  <em>now</em>). If  <code>from_date</code>  contains 22 June 2006, then the following will return “1 week”:</p>
<pre><code>{{ conference_date|timeuntil:from_date }}
</code></pre>
<p>Comparing offset-naive and offset-aware datetimes will return an empty string.</p>
<p>Minutes is the smallest unit used, and “0 minutes” will be returned for any date that is in the past relative to the comparison point.</p>
<h3 id="title"><code>title</code></h3>
<p>Converts a string into titlecase by making words start with an uppercase character and the remaining characters lowercase. This tag makes no effort to keep “trivial words” in lowercase.</p>
<p>For example:</p>
<pre><code>{{ value|title }}
</code></pre>
<p>If  <code>value</code>  is  <code>"my FIRST post"</code>, the output will be  <code>"My First Post"</code>.</p>
<h3 id="truncatechars"><code>truncatechars</code></h3>
<p>Truncates a string if it is longer than the specified number of characters. Truncated strings will end with a translatable ellipsis character (“…”).</p>
<p><strong>Argument:</strong>  Number of characters to truncate to</p>
<p>For example:</p>
<pre><code>{{ value|truncatechars:7 }}
</code></pre>
<p>If  <code>value</code>  is  <code>"Joel is a slug"</code>, the output will be  <code>"Joel i…"</code>.</p>
<h3 id="truncatechars_html"><code>truncatechars_html</code></h3>
<p>Similar to  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-truncatechars"><code>truncatechars</code></a>, except that it is aware of HTML tags. Any tags that are opened in the string and not closed before the truncation point are closed immediately after the truncation.</p>
<p>For example:</p>
<pre><code>{{ value|truncatechars_html:7 }}
</code></pre>
<p>If  <code>value</code>  is  <code>"&lt;p&gt;Joel is a slug&lt;/p&gt;"</code>, the output will be  <code>"&lt;p&gt;Joel i…&lt;/p&gt;"</code>.</p>
<p>Newlines in the HTML content will be preserved.</p>
<h3 id="truncatewords"><code>truncatewords</code></h3>
<p>Truncates a string after a certain number of words.</p>
<p><strong>Argument:</strong>  Number of words to truncate after</p>
<p>For example:</p>
<pre><code>{{ value|truncatewords:2 }}
</code></pre>
<p>If  <code>value</code>  is  <code>"Joel is a slug"</code>, the output will be  <code>"Joel is …"</code>.</p>
<p>Newlines within the string will be removed.</p>
<h3 id="truncatewords_html"><code>truncatewords_html</code></h3>
<p>Similar to  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-truncatewords"><code>truncatewords</code></a>, except that it is aware of HTML tags. Any tags that are opened in the string and not closed before the truncation point, are closed immediately after the truncation.</p>
<p>This is less efficient than  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-truncatewords"><code>truncatewords</code></a>, so should only be used when it is being passed HTML text.</p>
<p>For example:</p>
<pre><code>{{ value|truncatewords_html:2 }}
</code></pre>
<p>If  <code>value</code>  is  <code>"&lt;p&gt;Joel is a slug&lt;/p&gt;"</code>, the output will be  <code>"&lt;p&gt;Joel is …&lt;/p&gt;"</code>.</p>
<p>Newlines in the HTML content will be preserved.</p>
<h3 id="unordered_list"><code>unordered_list</code></h3>
<p>Recursively takes a self-nested list and returns an HTML unordered list – WITHOUT opening and closing </p><ul> tags.</ul><p></p>
<p>The list is assumed to be in the proper format. For example, if  <code>var</code>  contains  <code>['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']]</code>, then  <code>{{ var|unordered_list }}</code>  would return:</p>
<pre><code>&lt;li&gt;States
&lt;ul&gt;
     &lt;li&gt;Kansas
     &lt;ul&gt;
         &lt;li&gt;Lawrence&lt;/li&gt;
         &lt;li&gt;Topeka&lt;/li&gt;
     &lt;/ul&gt;
     &lt;/li&gt;
     &lt;li&gt;Illinois&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
</code></pre>
<h3 id="upper"><code>upper</code></h3>
<p>Converts a string into all uppercase.</p>
<p>For example:</p>
<pre><code>{{ value|upper }}
</code></pre>
<p>If  <code>value</code>  is  <code>"Joel is a slug"</code>, the output will be  <code>"JOEL IS A SLUG"</code>.</p>
<h3 id="urlencode"><code>urlencode</code></h3>
<p>Escapes a value for use in a URL.</p>
<p>For example:</p>
<pre><code>{{ value|urlencode }}
</code></pre>
<p>If  <code>value</code>  is  <code>"https://www.example.org/foo?a=b&amp;c=d"</code>, the output will be  <code>"https%3A//www.example.org/foo%3Fa%3Db%26c%3Dd"</code>.</p>
<p>An optional argument containing the characters which should not be escaped can be provided.</p>
<p>If not provided, the ‘/’ character is assumed safe. An empty string can be provided when  <em>all</em>  characters should be escaped. For example:</p>
<pre><code>{{ value|urlencode:"" }}
</code></pre>
<p>If  <code>value</code>  is  <code>"https://www.example.org/"</code>, the output will be  <code>"https%3A%2F%2Fwww.example.org%2F"</code>.</p>
<h3 id="urlize"><code>urlize</code></h3>
<p>Converts URLs and email addresses in text into clickable links.</p>
<p>This template tag works on links prefixed with  <code>http://</code>,  <code>https://</code>, or  <code>www.</code>. For example,  <code>https://goo.gl/aia1t</code>  will get converted but  <code>goo.gl/aia1t</code>  won’t.</p>
<p>It also supports domain-only links ending in one of the original top level domains (<code>.com</code>,  <code>.edu</code>,  <code>.gov</code>,  <code>.int</code>,  <code>.mil</code>,  <code>.net</code>, and  <code>.org</code>). For example,  <code>djangoproject.com</code>  gets converted.</p>
<p>Links can have trailing punctuation (periods, commas, close-parens) and leading punctuation (opening parens), and  <code>urlize</code>  will still do the right thing.</p>
<p>Links generated by  <code>urlize</code>  have a  <code>rel="nofollow"</code>  attribute added to them.</p>
<p>For example:</p>
<pre><code>{{ value|urlize }}
</code></pre>
<p>If  <code>value</code>  is  <code>"Check out www.djangoproject.com"</code>, the output will be  <code>"Check out &lt;a href="http://www.djangoproject.com" rel="nofollow"&gt;www.djangoproject.com&lt;/a&gt;"</code>.</p>
<p>In addition to web links,  <code>urlize</code>  also converts email addresses into  <code>mailto:</code>  links. If  <code>value</code>  is  <code>"Send questions to foo@example.com"</code>, the output will be  <code>"Send questions to &lt;a href="mailto:foo@example.com"&gt;foo@example.com&lt;/a&gt;"</code>.</p>
<p>The  <code>urlize</code>  filter also takes an optional parameter  <code>autoescape</code>. If  <code>autoescape</code>  is  <code>True</code>, the link text and URLs will be escaped using Django’s built-in  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-escape"><code>escape</code></a>  filter. The default value for  <code>autoescape</code>  is  <code>True</code>.</p>
<blockquote>
<p><em>Note</em><br>
<em>If  <code>urlize</code>  is applied to text that already contains HTML markup, or to email addresses that contain single quotes (<code>'</code>), things won’t work as expected. Apply this filter only to plain text.</em></p>
</blockquote>
<h3 id="urlizetrunc"><code>urlizetrunc</code></h3>
<p>Converts URLs and email addresses into clickable links just like  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#urlize">urlize</a>, but truncates URLs longer than the given character limit.</p>
<p><strong>Argument:</strong>  Number of characters that link text should be truncated to, including the ellipsis that’s added if truncation is necessary.</p>
<p>For example:</p>
<pre><code>{{ value|urlizetrunc:15 }}
</code></pre>
<p>If  <code>value</code>  is  <code>"Check out www.djangoproject.com"</code>, the output would be  <code>'Check out &lt;a href="http://www.djangoproject.com" rel="nofollow"&gt;www.djangoproj…&lt;/a&gt;'</code>.</p>
<p>As with  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#urlize">urlize</a>, this filter should only be applied to plain text.</p>
<h3 id="wordcount"><code>wordcount</code></h3>
<p>Returns the number of words.</p>
<p>For example:</p>
<pre><code>{{ value|wordcount }}
</code></pre>
<p>If  <code>value</code>  is  <code>"Joel is a slug"</code>, the output will be  <code>4</code>.</p>
<h3 id="wordwrap"><code>wordwrap</code></h3>
<p>Wraps words at specified line length.</p>
<p><strong>Argument:</strong>  number of characters at which to wrap the text</p>
<p>For example:</p>
<pre><code>{{ value|wordwrap:5 }}
</code></pre>
<p>If  <code>value</code>  is  <code>Joel is a slug</code>, the output would be:</p>
<pre><code>Joel
is a
slug
</code></pre>
<pre><code>&lt;/div&gt;
</code></pre>
  

# Built-in template tags and filters
This document describes Django’s built-in template tags and filters. It is recommended that you use the  [automatic documentation](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/admindocs/), if available, as this will also include documentation for any custom tags or filters installed.
<h2 id="built-in-tag-reference">Built-in tag reference</h2>
<h3 id="autoescape"><code>autoescape</code></h3>
<p>Controls the current auto-escaping behavior. This tag takes either  <code>on</code>  or  <code>off</code>  as an argument and that determines whether auto-escaping is in effect inside the block. The block is closed with an  <code>endautoescape</code>  ending tag.</p>
<p>When auto-escaping is in effect, all variable content has HTML escaping applied to it before placing the result into the output (but after any filters have been applied). This is equivalent to manually applying the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-escape"><code>escape</code></a>  filter to each variable.</p>
<p>The only exceptions are variables that are already marked as “safe” from escaping, either by the code that populated the variable, or because it has had the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-safe"><code>safe</code></a>  or  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-escape"><code>escape</code></a>  filters applied.</p>
<p>Sample usage:</p>
<pre><code>{% autoescape on %}
    {{ body }}
{% endautoescape %}
</code></pre>
<hr>
<h3 id="comment"><code>comment</code></h3>
<p>Ignores everything between  <code>{% comment %}</code>  and  <code>{% endcomment %}</code>. An optional note may be inserted in the first tag. For example, this is useful when commenting out code for documenting why the code was disabled.</p>
<p>Sample usage:</p>
<pre><code>&lt;p&gt;Rendered text with {{ pub_date|date:"c" }}&lt;/p&gt;
{% comment "Optional note" %}
    &lt;p&gt;Commented out text with {{ create_date|date:"c" }}&lt;/p&gt;
{% endcomment %}
</code></pre>
<p><code>comment</code>  tags cannot be nested.</p>
<hr>
<h3 id="cycle"><code>cycle</code></h3>
<p>Produces one of its arguments each time this tag is encountered. The first argument is produced on the first encounter, the second argument on the second encounter, and so forth. Once all arguments are exhausted, the tag cycles to the first argument and produces it again.</p>
<p>This tag is particularly useful in a loop:</p>
<pre><code>{% for o in some_list %}
    &lt;tr class="{% cycle 'row1' 'row2' %}"&gt;
        ...
    &lt;/tr&gt;
{% endfor %}
</code></pre>
<p>The first iteration produces HTML that refers to class  <code>row1</code>, the second to  <code>row2</code>, the third to  <code>row1</code>  again, and so on for each iteration of the loop.</p>
<p>You can use variables, too. For example, if you have two template variables,  <code>rowvalue1</code>  and  <code>rowvalue2</code>, you can alternate between their values like this:</p>
<pre><code>{% for o in some_list %}
    &lt;tr class="{% cycle rowvalue1 rowvalue2 %}"&gt;
        ...
    &lt;/tr&gt;
{% endfor %}
</code></pre>
<p>Variables included in the cycle will be escaped. You can disable auto-escaping with:</p>
<pre><code>{% for o in some_list %}
    &lt;tr class="{% autoescape off %}{% cycle rowvalue1 rowvalue2 %}{% endautoescape %}"&gt;
        ...
    &lt;/tr&gt;
{% endfor %}
</code></pre>
<p>You can mix variables and strings:</p>
<pre><code>{% for o in some_list %}
    &lt;tr class="{% cycle 'row1' rowvalue2 'row3' %}"&gt;
        ...
    &lt;/tr&gt;
{% endfor %}
</code></pre>
<p>In some cases you might want to refer to the current value of a cycle without advancing to the next value. To do this, give the  <code>{% cycle %}</code>  tag a name, using “as”, like this:</p>
<pre><code>{% cycle 'row1' 'row2' as rowcolors %}
</code></pre>
<p>From then on, you can insert the current value of the cycle wherever you’d like in your template by referencing the cycle name as a context variable. If you want to move the cycle to the next value independently of the original  <code>cycle</code>  tag, you can use another  <code>cycle</code>  tag and specify the name of the variable. So, the following template:</p>
<pre><code>&lt;tr&gt;
    &lt;td class="{% cycle 'row1' 'row2' as rowcolors %}"&gt;...&lt;/td&gt;
    &lt;td class="{{ rowcolors }}"&gt;...&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
    &lt;td class="{% cycle rowcolors %}"&gt;...&lt;/td&gt;
    &lt;td class="{{ rowcolors }}"&gt;...&lt;/td&gt;
&lt;/tr&gt;
</code></pre>
<p>would output:</p>
<pre><code>&lt;tr&gt;
    &lt;td class="row1"&gt;...&lt;/td&gt;
    &lt;td class="row1"&gt;...&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
    &lt;td class="row2"&gt;...&lt;/td&gt;
    &lt;td class="row2"&gt;...&lt;/td&gt;
&lt;/tr&gt;
</code></pre>
<p>You can use any number of values in a  <code>cycle</code>  tag, separated by spaces. Values enclosed in single quotes (<code>'</code>) or double quotes (<code>"</code>) are treated as string literals, while values without quotes are treated as template variables.</p>
<p>By default, when you use the  <code>as</code>  keyword with the cycle tag, the usage of  <code>{% cycle %}</code>  that initiates the cycle will itself produce the first value in the cycle. This could be a problem if you want to use the value in a nested loop or an included template. If you only want to declare the cycle but not produce the first value, you can add a  <code>silent</code>  keyword as the last keyword in the tag. For example:</p>
<pre><code>{% for obj in some_list %}
    {% cycle 'row1' 'row2' as rowcolors silent %}
    &lt;tr class="{{ rowcolors }}"&gt;{% include "subtemplate.html" %}&lt;/tr&gt;
{% endfor %}
</code></pre>
<p>This will output a list of  <code>&lt;tr&gt;</code>  elements with  <code>class</code>  alternating between  <code>row1</code>  and  <code>row2</code>. The subtemplate will have access to  <code>rowcolors</code>  in its context and the value will match the class of the  <code>&lt;tr&gt;</code>  that encloses it. If the  <code>silent</code>  keyword were to be omitted,  <code>row1</code>  and  <code>row2</code>  would be emitted as normal text, outside the  <code>&lt;tr&gt;</code>  element.</p>
<p>When the silent keyword is used on a cycle definition, the silence automatically applies to all subsequent uses of that specific cycle tag. The following template would output  <em>nothing</em>, even though the second call to  <code>{% cycle %}</code>  doesn’t specify  <code>silent</code>:</p>
<pre><code>{% cycle 'row1' 'row2' as rowcolors silent %}
{% cycle rowcolors %}
</code></pre>
<p>You can use the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-resetcycle"><code>resetcycle</code></a>  tag to make a  <code>{% cycle %}</code>  tag restart from its first value when it’s next encountered.</p>
<hr>
<h3 id="filter"><code>filter</code></h3>
<p>Filters the contents of the block through one or more filters. Multiple filters can be specified with pipes and filters can have arguments, just as in variable syntax.</p>
<p>Note that the block includes  <em>all</em>  the text between the  <code>filter</code>  and  <code>endfilter</code>  tags.</p>
<p>Sample usage:</p>
<pre><code>{% filter force_escape|lower %}
    This text will be HTML-escaped, and will appear in all lowercase.
{% endfilter %}
</code></pre>
<blockquote>
<p><em>Note</em><br>
<em>The <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-escape"><code>escape</code></a> and <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-safe"><code>safe</code></a> filters are not acceptable arguments. Instead, use the <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-autoescape"><code>autoescape</code></a> tag to manage autoescaping for blocks of template code.</em></p>
</blockquote>
<hr>
<h3 id="firstof"><code>firstof</code></h3>
<p>Outputs the first argument variable that is not “false” (i.e. exists, is not empty, is not a false boolean value, and is not a zero numeric value). Outputs nothing if all the passed variables are “false”.</p>
<p>Sample usage:</p>
<pre><code>{% firstof var1 var2 var3 %}
</code></pre>
<p>This is equivalent to:</p>
<pre><code>{% if var1 %}
    {{ var1 }}
{% elif var2 %}
    {{ var2 }}
{% elif var3 %}
    {{ var3 }}
{% endif %}
</code></pre>
<p>You can also use a literal string as a fallback value in case all passed variables are False:</p>
<pre><code>{% firstof var1 var2 var3 "fallback value" %}
</code></pre>
<p>This tag auto-escapes variable values. You can disable auto-escaping with:</p>
<pre><code>{% autoescape off %}
    {% firstof var1 var2 var3 "&lt;strong&gt;fallback value&lt;/strong&gt;" %}
{% endautoescape %}
</code></pre>
<p>Or if only some variables should be escaped, you can use:</p>
<pre><code>{% firstof var1 var2|safe var3 "&lt;strong&gt;fallback value&lt;/strong&gt;"|safe %}
</code></pre>
<p>You can use the syntax  <code>{% firstof var1 var2 var3 as value %}</code>  to store the output inside a variable.</p>
<hr>
<h3 id="for"><code>for</code></h3>
<p>Loops over each item in an array, making the item available in a context variable. For example, to display a list of athletes provided in  <code>athlete_list</code>:</p>
<pre><code>&lt;ul&gt;
{% for athlete in athlete_list %}
    &lt;li&gt;{{ athlete.name }}&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
</code></pre>
<p>You can loop over a list in reverse by using  <code>{% for obj in list reversed %}</code>.</p>
<p>If you need to loop over a list of lists, you can unpack the values in each sublist into individual variables. For example, if your context contains a list of (x,y) coordinates called  <code>points</code>, you could use the following to output the list of points:</p>
<pre><code>{% for x, y in points %}
    There is a point at {{ x }},{{ y }}
{% endfor %}
</code></pre>
<p>This can also be useful if you need to access the items in a dictionary. For example, if your context contained a dictionary  <code>data</code>, the following would display the keys and values of the dictionary:</p>
<pre><code>{% for key, value in data.items %}
    {{ key }}: {{ value }}
{% endfor %}
</code></pre>
<p>Keep in mind that for the dot operator, dictionary key lookup takes precedence over method lookup. Therefore if the  <code>data</code>  dictionary contains a key named  <code>'items'</code>,  <code>data.items</code>  will return  <code>data['items']</code>  instead of  <code>data.items()</code>. Avoid adding keys that are named like dictionary methods if you want to use those methods in a template (<code>items</code>,  <code>values</code>,  <code>keys</code>, etc.). Read more about the lookup order of the dot operator in the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/language/#template-variables">documentation of template variables</a>.</p>
<p>The for loop sets a number of variables available within the loop:</p>

<table>
<thead>
<tr>
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>forloop.counter</code></td>
<td>The current iteration of the loop (1-indexed)</td>
</tr>
<tr>
<td><code>forloop.revcounter</code></td>
<td>The number of iterations from the end of the loop (1-indexed)</td>
</tr>
<tr>
<td><code>forloop.first</code></td>
<td>True if this is the first time through the loop</td>
</tr>
<tr>
<td><code>forloop.parentloop</code></td>
<td>For nested loops, this is the loop surrounding the current one</td>
</tr>
</tbody>
</table><hr>
<h3 id="for--…--empty"><code>for</code>  …  <code>empty</code></h3>
<p>The  <code>for</code>  tag can take an optional  <code>{% empty %}</code>  clause whose text is displayed if the given array is empty or could not be found:</p>
<pre><code>&lt;ul&gt;
{% for athlete in athlete_list %}
    &lt;li&gt;{{ athlete.name }}&lt;/li&gt;
{% empty %}
    &lt;li&gt;Sorry, no athletes in this list.&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
</code></pre>
<p>The above is equivalent to – but shorter, cleaner, and possibly faster than – the following:</p>
<pre><code>&lt;ul&gt;
  {% if athlete_list %}
    {% for athlete in athlete_list %}
      &lt;li&gt;{{ athlete.name }}&lt;/li&gt;
    {% endfor %}
  {% else %}
    &lt;li&gt;Sorry, no athletes in this list.&lt;/li&gt;
  {% endif %}
&lt;/ul&gt;
</code></pre>
<hr>
<h3 id="if"><code>if</code></h3>
<p>The  <code>{% if %}</code>  tag evaluates a variable, and if that variable is “true” (i.e. exists, is not empty, and is not a false boolean value) the contents of the block are output:</p>
<pre><code>{% if athlete_list %}
    Number of athletes: {{ athlete_list|length }}
{% elif athlete_in_locker_room_list %}
    Athletes should be out of the locker room soon!
{% else %}
    No athletes.
{% endif %}
</code></pre>
<p>In the above, if  <code>athlete_list</code>  is not empty, the number of athletes will be displayed by the  <code>{{ athlete_list|length }}</code>  variable.</p>
<p>As you can see, the  <code>if</code>  tag may take one or several  <code>{% elif %}</code>  clauses, as well as an  <code>{% else %}</code>  clause that will be displayed if all previous conditions fail. These clauses are optional.</p>
<hr>
<h4 id="boolean-operators">Boolean operators</h4>
<p><a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-if"><code>if</code></a>  tags may use  <code>and</code>,  <code>or</code>  or  <code>not</code>  to test a number of variables or to negate a given variable:</p>
<pre><code>{% if athlete_list and coach_list %}
    Both athletes and coaches are available.
{% endif %}

{% if not athlete_list %}
    There are no athletes.
{% endif %}

{% if athlete_list or coach_list %}
    There are some athletes or some coaches.
{% endif %}

{% if not athlete_list or coach_list %}
    There are no athletes or there are some coaches.
{% endif %}

{% if athlete_list and not coach_list %}
    There are some athletes and absolutely no coaches.
{% endif %}
</code></pre>
<p>Use of both  <code>and</code>  and  <code>or</code>  clauses within the same tag is allowed, with  <code>and</code>  having higher precedence than  <code>or</code>  e.g.:</p>
<pre><code>{% if athlete_list and coach_list or cheerleader_list %}
</code></pre>
<p>will be interpreted like:</p>
<pre><code>if (athlete_list and coach_list) or cheerleader_list
</code></pre>
<p>Use of actual parentheses in the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-if"><code>if</code></a>  tag is invalid syntax. If you need them to indicate precedence, you should use nested  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-if"><code>if</code></a>  tags.</p>
<p><a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-if"><code>if</code></a>  tags may also use the operators  <code>==</code>,  <code>!=</code>,  <code>&lt;</code>,  <code>&gt;</code>,  <code>&lt;=</code>,  <code>&gt;=</code>,  <code>in</code>,  <code>not in</code>,  <code>is</code>, and  <code>is not</code>  which work as follows:</p>
<h5 id="operator"><code>==</code>  operator</h5>
<p>Equality. Example:</p>
<pre><code>{% if somevar == "x" %}
  This appears if variable somevar equals the string "x"
{% endif %}
</code></pre>
<h5 id="operator-1"><code>!=</code>  operator</h5>
<p>Inequality. Example:</p>
<pre><code>{% if somevar != "x" %}
  This appears if variable somevar does not equal the string "x",
  or if somevar is not found in the context
{% endif %}
</code></pre>
<h5 id="operator-2"><code>&lt;</code>  operator</h5>
<p>Less than. Example:</p>
<pre><code>{% if somevar &lt; 100 %}
  This appears if variable somevar is less than 100.
{% endif %}
</code></pre>
<h5 id="operator-3"><code>&gt;</code>  operator</h5>
<p>Greater than. Example:</p>
<pre><code>{% if somevar &gt; 0 %}
  This appears if variable somevar is greater than 0.
{% endif %}
</code></pre>
<h5 id="operator-4"><code>&lt;=</code>  operator</h5>
<p>Less than or equal to. Example:</p>
<pre><code>{% if somevar &lt;= 100 %}
  This appears if variable somevar is less than 100 or equal to 100.
{% endif %}
</code></pre>
<h5 id="operator-5"><code>&gt;=</code>  operator</h5>
<p>Greater than or equal to. Example:</p>
<pre><code>{% if somevar &gt;= 1 %}
  This appears if variable somevar is greater than 1 or equal to 1.
{% endif %}
</code></pre>
<h5 id="in--operator"><code>in</code>  operator</h5>
<p>Contained within. This operator is supported by many Python containers to test whether the given value is in the container. The following are some examples of how  <code>x in y</code>  will be interpreted:</p>
<pre><code>{% if "bc" in "abcdef" %}
  This appears since "bc" is a substring of "abcdef"
{% endif %}

{% if "hello" in greetings %}
  If greetings is a list or set, one element of which is the string
  "hello", this will appear.
{% endif %}

{% if user in users %}
  If users is a QuerySet, this will appear if user is an
  instance that belongs to the QuerySet.
{% endif %}
</code></pre>
<h5 id="not-in--operator"><code>not in</code>  operator</h5>
<p>Not contained within. This is the negation of the  <code>in</code>  operator.</p>
<h5 id="is--operator"><code>is</code>  operator</h5>
<p>Object identity. Tests if two values are the same object. Example:</p>
<pre><code>{% if somevar is True %}
  This appears if and only if somevar is True.
{% endif %}

{% if somevar is None %}
  This appears if somevar is None, or if somevar is not found in the context.
{% endif %}
</code></pre>
<h5 id="is-not--operator"><code>is not</code>  operator</h5>
<p>Negated object identity. Tests if two values are not the same object. This is the negation of the  <code>is</code>  operator. Example:</p>
<pre><code>{% if somevar is not True %}
  This appears if somevar is not True, or if somevar is not found in the
  context.
{% endif %}

{% if somevar is not None %}
  This appears if and only if somevar is not None.
{% endif %}
</code></pre>
<hr>
<h4 id="filters">Filters</h4>
<p>You can also use filters in the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-if"><code>if</code></a>  expression. For example:</p>
<pre><code>{% if messages|length &gt;= 100 %}
   You have lots of messages today!
{% endif %}
</code></pre>
<h4 id="complex-expressions-headline">Complex expressions headline")</h4>
<p>All of the above can be combined to form complex expressions. For such expressions, it can be important to know how the operators are grouped when the expression is evaluated - that is, the precedence rules. The precedence of the operators, from lowest to highest, is as follows:</p>
<ul>
<li><code>or</code></li>
<li><code>and</code></li>
<li><code>not</code></li>
<li><code>in</code></li>
<li><code>==</code>,  <code>!=</code>,  <code>&lt;</code>,  <code>&gt;</code>,  <code>&lt;=</code>,  <code>&gt;=</code></li>
</ul>
<p>(This follows Python exactly). So, for example, the following complex  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-if"><code>if</code></a>  tag:</p>
<p>{% if a == b or c == d and e %}</p>
<p>…will be interpreted as:</p>
<p>(a == b) or ((c == d) and e)</p>
<p>If you need different precedence, you will need to use nested  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-if"><code>if</code></a>  tags. Sometimes that is better for clarity anyway, for the sake of those who do not know the precedence rules.</p>
<p>The comparison operators cannot be ‘chained’ like in Python or in mathematical notation. For example, instead of using:</p>
<p>{% if a &gt; b &gt; c %}  (WRONG)</p>
<p>you should use:</p>
<p>{% if a &gt; b and b &gt; c %}</p>
<h3 id="include"><code>include</code></h3>
<p>Loads a template and renders it with the current context. This is a way of “including” other templates within a template.</p>
<p>This example includes the contents of the template  <code>"foo/bar.html"</code>:</p>
<pre><code>{% include "foo/bar.html" %}
</code></pre>
<p>This example includes the contents of the template whose name is contained in the variable  <code>template_name</code>:</p>
<pre><code>{% include template_name %}
</code></pre>
<p>You can pass additional context to the template using keyword arguments:</p>
<pre><code>{% include "name_snippet.html" with person="Jane" greeting="Hello" %}
</code></pre>
<p>If you want to render the context only with the variables provided (or even no variables at all), use the  <code>only</code>  option. No other variables are available to the included template:</p>
<pre><code>{% include "name_snippet.html" with greeting="Hi" only %}
</code></pre>
<hr>
<h3 id="lorem"><code>lorem</code></h3>
<p>Displays random “lorem ipsum” Latin text. This is useful for providing sample data in templates.</p>
<p>Usage:</p>
<pre><code>{% lorem [count] [method] [random] %}
</code></pre>
<p>Examples</p>
<ul>
<li><code>{% lorem %}</code>  will output the common “lorem ipsum” paragraph.</li>
<li><code>{% lorem 3 p %}</code>  will output the common “lorem ipsum” paragraph and two random paragraphs each wrapped in HTML  <code>&lt;p&gt;</code>  tags.</li>
<li><code>{% lorem 2 w random %}</code>  will output two random Latin words.</li>
</ul>
<hr>
<h3 id="regroup"><code>regroup</code></h3>
<p>Regroups a list of alike objects by a common attribute.</p>
<p>This complex tag is best illustrated by way of an example: say that  <code>cities</code>  is a list of cities represented by dictionaries containing  <code>"name"</code>,  <code>"population"</code>, and  <code>"country"</code>  keys:</p>
<pre><code>cities = [
    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
]
</code></pre>
<p>…and you’d like to display a hierarchical list that is ordered by country, like this:</p>
<pre><code>-   India
    -   Mumbai: 19,000,000
    -   Calcutta: 15,000,000
-   USA
    -   New York: 20,000,000
    -   Chicago: 7,000,000
-   Japan
    -   Tokyo: 33,000,000
</code></pre>
<p>You can use the  <code>{% regroup %}</code>  tag to group the list of cities by country. The following snippet of template code would accomplish this:</p>
<pre><code>{% regroup cities by country as country_list %}

&lt;ul&gt;
{% for country in country_list %}
    &lt;li&gt;{{ country.grouper }}
    &lt;ul&gt;
        {% for city in country.list %}
          &lt;li&gt;{{ city.name }}: {{ city.population }}&lt;/li&gt;
        {% endfor %}
    &lt;/ul&gt;
    &lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
</code></pre>
<p>Let’s walk through this example.  <code>{% regroup %}</code>  takes three arguments: the list you want to regroup, the attribute to group by, and the name of the resulting list. Here, we’re regrouping the  <code>cities</code>  list by the  <code>country</code>  attribute and calling the result  <code>country_list</code>.</p>
<p><code>{% regroup %}</code>  produces a list (in this case,  <code>country_list</code>) of  <strong>group objects</strong>. Group objects are instances of  <a href="https://docs.python.org/3/library/collections.html#collections.namedtuple" title="(in Python v3.9)"><code>namedtuple()</code></a>  with two fields:</p>
<ul>
<li><code>grouper</code>  – the item that was grouped by (e.g., the string “India” or “Japan”).</li>
<li><code>list</code>  – a list of all items in this group (e.g., a list of all cities with country=’India’).</li>
</ul>
<p>Because  <code>{% regroup %}</code>  produces  <a href="https://docs.python.org/3/library/collections.html#collections.namedtuple" title="(in Python v3.9)"><code>namedtuple()</code></a>  objects, you can also write the previous example as:</p>
<p>{% regroup cities by country as country_list %}</p>
<pre><code>&lt;ul&gt;
{% for country, local_cities in country_list %}
    &lt;li&gt;{{ country }}
    &lt;ul&gt;
        {% for city in local_cities %}
          &lt;li&gt;{{ city.name }}: {{ city.population }}&lt;/li&gt;
        {% endfor %}
    &lt;/ul&gt;
    &lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
</code></pre>
<p>Note that  <code>{% regroup %}</code>  does not order its input! Our example relies on the fact that the  <code>cities</code>  list was ordered by  <code>country</code>  in the first place. If the  <code>cities</code>  list did  <em>not</em>  order its members by  <code>country</code>, the regrouping would naively display more than one group for a single country. For example, say the  <code>cities</code>  list was set to this (note that the countries are not grouped together):</p>
<pre><code>cities = [
    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
]
</code></pre>
<p>With this input for  <code>cities</code>, the example  <code>{% regroup %}</code>  template code above would result in the following output:</p>
<pre><code>-   India
    -   Mumbai: 19,000,000
-   USA
    -   New York: 20,000,000
-   India
    -   Calcutta: 15,000,000
-   USA
    -   Chicago: 7,000,000
-   Japan
    -   Tokyo: 33,000,000
</code></pre>
<p>The easiest solution to this gotcha is to make sure in your view code that the data is ordered according to how you want to display it.</p>
<p>Another solution is to sort the data in the template using the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-dictsort"><code>dictsort</code></a>  filter, if your data is in a list of dictionaries:</p>
<pre><code>{% regroup cities|dictsort:"country" by country as country_list %}
</code></pre>
<hr>
<h3 id="resetcycle"><code>resetcycle</code></h3>
<p>Resets a previous  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#cycle">cycle</a>  so that it restarts from its first item at its next encounter. Without arguments,  <code>{% resetcycle %}</code>  will reset the last  <code>{% cycle %}</code>  defined in the template.</p>
<p>Example usage:</p>
<pre><code>{% for coach in coach_list %}
    &lt;h1&gt;{{ coach.name }}&lt;/h1&gt;
    {% for athlete in coach.athlete_set.all %}
        &lt;p class="{% cycle 'odd' 'even' %}"&gt;{{ athlete.name }}&lt;/p&gt;
    {% endfor %}
    {% resetcycle %}
{% endfor %}
</code></pre>
<p>This example would return this HTML:</p>
<pre><code>&lt;h1&gt;José Mourinho&lt;/h1&gt;
&lt;p class="odd"&gt;Thibaut Courtois&lt;/p&gt;
&lt;p class="even"&gt;John Terry&lt;/p&gt;
&lt;p class="odd"&gt;Eden Hazard&lt;/p&gt;

&lt;h1&gt;Carlo Ancelotti&lt;/h1&gt;
&lt;p class="odd"&gt;Manuel Neuer&lt;/p&gt;
&lt;p class="even"&gt;Thomas Müller&lt;/p&gt;
</code></pre>
<p>Notice how the first block ends with  <code>class="odd"</code>  and the new one starts with  <code>class="odd"</code>. Without the  <code>{% resetcycle %}</code>  tag, the second block would start with  <code>class="even"</code>.</p>
<p>You can also reset named cycle tags:</p>
<pre><code>{% for item in list %}
    &lt;p class="{% cycle 'odd' 'even' as stripe %}  {% cycle 'major' 'minor' 'minor' 'minor' 'minor' as tick %}"&gt;
        {{ item.data }}
    &lt;/p&gt;
    {% ifchanged item.category %}
        &lt;h1&gt;{{ item.category }}&lt;/h1&gt;
        {% if not forloop.first %}{% resetcycle tick %}{% endif %}
    {% endifchanged %}
{% endfor %}
</code></pre>
<p>In this example, we have both the alternating odd/even rows and a “major” row every fifth row. Only the five-row cycle is reset when a category changes.</p>
<hr>
<h3 id="spaceless"><code>spaceless</code></h3>
<p>Removes whitespace between HTML tags. This includes tab characters and newlines.</p>
<p>Example usage:</p>
<pre><code>{% spaceless %}
    &lt;p&gt;
        &lt;a href="foo/"&gt;Foo&lt;/a&gt;
    &lt;/p&gt;
{% endspaceless %}
</code></pre>
<p>This example would return this HTML:</p>
<pre><code>&lt;p&gt;&lt;a href="foo/"&gt;Foo&lt;/a&gt;&lt;/p&gt;
</code></pre>
<hr>
<h3 id="widthratio"><code>widthratio</code></h3>
<p>For creating bar charts and such, this tag calculates the ratio of a given value to a maximum value, and then applies that ratio to a constant.</p>
<p>For example:</p>
<pre><code>&lt;img src="bar.png" alt="Bar"
     height="10" width="{% widthratio this_value max_value max_width %}"&gt;
</code></pre>
<p>If  <code>this_value</code>  is 175,  <code>max_value</code>  is 200, and  <code>max_width</code>  is 100, the image in the above example will be 88 pixels wide (because 175/200 = .875; .875 * 100 = 87.5 which is rounded up to 88).</p>
<p>In some cases you might want to capture the result of  <code>widthratio</code>  in a variable. It can be useful, for instance, in a  <a href="https://docs.djangoproject.com/en/3.1/topics/i18n/translation/#std:templatetag-blocktranslate"><code>blocktranslate</code></a>  like this:</p>
<pre><code>{% widthratio this_value max_value max_width as width %}
{% blocktranslate %}The width is: {{ width }}{% endblocktranslate %}
</code></pre>
<hr>
<h3 id="with"><code>with</code></h3>
<p>Caches a complex variable under a simpler name. This is useful when accessing an “expensive” method (e.g., one that hits the database) multiple times.</p>
<p>For example:</p>
<pre><code>{% with total=business.employees.count %}
    {{ total }} employee{{ total|pluralize }}
{% endwith %}
</code></pre>
<p>The populated variable (in the example above,  <code>total</code>) is only available between the  <code>{% with %}</code>  and  <code>{% endwith %}</code>  tags.</p>
<p>You can assign more than one context variable:</p>
<pre><code>{% with alpha=1 beta=2 %}
    ...
{% endwith %}
</code></pre>
<h2 id="built-in-filter-reference">Built-in filter reference</h2>
<h3 id="add"><code>add</code></h3>
<p>Adds the argument to the value.</p>
<p>For example:</p>
<pre><code>{{ value|add:"2" }}
</code></pre>
<p>If  <code>value</code>  is  <code>4</code>, then the output will be  <code>6</code>.</p>
<p>This filter will first try to coerce both values to integers. If this fails, it’ll attempt to add the values together anyway. This will work on some data types (strings, list, etc.) and fail on others. If it fails, the result will be an empty string.</p>
<p>For example, if we have:</p>
<pre><code>{{ first|add:second }}
</code></pre>
<p>and  <code>first</code>  is  <code>[1, 2, 3]</code>  and  <code>second</code>  is  <code>[4, 5, 6]</code>, then the output will be  <code>[1, 2, 3, 4, 5, 6]</code>.</p>
<p>Warning</p>
<p>Strings that can be coerced to integers will be  <strong>summed</strong>, not concatenated, as in the first example above.</p>
<h3 id="addslashes"><code>addslashes</code></h3>
<p>Adds slashes before quotes. Useful for escaping strings in CSV, for example.</p>
<p>For example:</p>
<pre><code>{{ value|addslashes }}
</code></pre>
<p>If  <code>value</code>  is  <code>"I'm using Django"</code>, the output will be  <code>"I\'m using Django"</code>.</p>
<h3 id="capfirst"><code>capfirst</code></h3>
<p>Capitalizes the first character of the value. If the first character is not a letter, this filter has no effect.</p>
<p>For example:</p>
<p>{{ value|capfirst }}</p>
<p>If  <code>value</code>  is  <code>"django"</code>, the output will be  <code>"Django"</code>.</p>
<hr>
<h3 id="cut"><code>cut</code></h3>
<p>Removes all values of arg from the given string.</p>
<p>For example:</p>
<pre><code>{{ value|cut:" " }}
</code></pre>
<p>If  <code>value</code>  is  <code>"String with spaces"</code>, the output will be  <code>"Stringwithspaces"</code>.</p>
<h3 id="default"><code>default</code></h3>
<p>If value evaluates to  <code>False</code>, uses the given default. Otherwise, uses the value.</p>
<p>For example:</p>
<pre><code>{{ value|default:"nothing" }}
</code></pre>
<p>If  <code>value</code>  is  <code>""</code>  (the empty string), the output will be  <code>nothing</code>.</p>
<h3 id="default_if_none"><code>default_if_none</code></h3>
<p>If (and only if) value is  <code>None</code>, uses the given default. Otherwise, uses the value.</p>
<p>Note that if an empty string is given, the default value will  <em>not</em>  be used. Use the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-default"><code>default</code></a>  filter if you want to fallback for empty strings.</p>
<p>For example:</p>
<p>{{ value|default_if_none:“nothing” }}</p>
<p>If  <code>value</code>  is  <code>None</code>, the output will be  <code>nothing</code>.</p>
<h3 id="dictsort"><code>dictsort</code></h3>
<p>Takes a list of dictionaries and returns that list sorted by the key given in the argument.</p>
<p>For example:</p>
<pre><code>{{ value|dictsort:"name" }}

If  `value`  is:

[
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
]
</code></pre>
<p>then the output would be:</p>
<pre><code>[
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
    {'name': 'zed', 'age': 19},
]
</code></pre>
<p>You can also do more complicated things like:</p>
<pre><code>{% for book in books|dictsort:"author.age" %}
    * {{ book.title }} ({{ book.author.name }})
{% endfor %}

If  `books`  is:

[
    {'title': '1984', 'author': {'name': 'George', 'age': 45}},
    {'title': 'Timequake', 'author': {'name': 'Kurt', 'age': 75}},
    {'title': 'Alice', 'author': {'name': 'Lewis', 'age': 33}},
]
</code></pre>
<p>then the output would be:</p>
<pre><code>* Alice (Lewis)
* 1984 (George)
* Timequake (Kurt)
</code></pre>
<p><code>dictsort</code>  can also order a list of lists (or any other object implementing  <code>__getitem__()</code>) by elements at specified index. For example:</p>
<pre><code>{{ value|dictsort:0 }}

If  `value`  is:

[
    ('a', '42'),
    ('c', 'string'),
    ('b', 'foo'),
]
</code></pre>
<p>then the output would be:</p>
<pre><code>[
    ('a', '42'),
    ('b', 'foo'),
    ('c', 'string'),
]
</code></pre>
<p>You must pass the index as an integer rather than a string. The following produce empty output:</p>
<pre><code>{{ values|dictsort:"0" }}
</code></pre>
<h3 id="dictsortreversed"><code>dictsortreversed</code></h3>
<p>Takes a list of dictionaries and returns that list sorted in reverse order by the key given in the argument. This works exactly the same as the above filter, but the returned value will be in reverse order.</p>
<h3 id="divisibleby"><code>divisibleby</code></h3>
<p>Returns  <code>True</code>  if the value is divisible by the argument.</p>
<p>For example:</p>
<pre><code>{{ value|divisibleby:"3" }}
</code></pre>
<p>If  <code>value</code>  is  <code>21</code>, the output would be  <code>True</code>.</p>
<h3 id="escape"><code>escape</code></h3>
<p>Escapes a string’s HTML. Specifically, it makes these replacements:</p>
<ul>
<li><code>&lt;</code>  is converted to  <code>&amp;lt;</code></li>
<li><code>&gt;</code>  is converted to  <code>&amp;gt;</code></li>
<li><code>'</code>  (single quote) is converted to  <code>&amp;#x27;</code></li>
<li><code>"</code>  (double quote) is converted to  <code>&amp;quot;</code></li>
<li><code>&amp;</code>  is converted to  <code>&amp;amp;</code></li>
</ul>
<p>Applying  <code>escape</code>  to a variable that would normally have auto-escaping applied to the result will only result in one round of escaping being done. So it is safe to use this function even in auto-escaping environments. If you want multiple escaping passes to be applied, use the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-force_escape"><code>force_escape</code></a>  filter.</p>
<p>For example, you can apply  <code>escape</code>  to fields when  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-autoescape"><code>autoescape</code></a>  is off:</p>
<pre><code>{% autoescape off %}
    {{ title|escape }}
{% endautoescape %}
</code></pre>
<h3 id="escapejs"><code>escapejs</code></h3>
<p>Escapes characters for use in JavaScript strings. This does  <em>not</em>  make the string safe for use in HTML or JavaScript template literals, but does protect you from syntax errors when using templates to generate JavaScript/JSON.</p>
<p>For example:</p>
<pre><code>{{ value|escapejs }}
</code></pre>
<p>If  <code>value</code>  is  <code>"testing\r\njavascript 'string\" &lt;b&gt;escaping&lt;/b&gt;"</code>, the output will be  <code>"testing\\u000D\\u000Ajavascript \\u0027string\\u0022 \\u003Cb\\u003Eescaping\\u003C/b\\u003E"</code>.</p>
<h3 id="filesizeformat"><code>filesizeformat</code></h3>
<p>Formats the value like a ‘human-readable’ file size (i.e.  <code>'13 KB'</code>,  <code>'4.1 MB'</code>,  <code>'102 bytes'</code>, etc.).</p>
<p>For example:</p>
<pre><code>{{ value|filesizeformat }}
</code></pre>
<p>If  <code>value</code>  is 123456789, the output would be  <code>117.7 MB</code>.</p>
<p>File sizes and SI units</p>
<p>Strictly speaking,  <code>filesizeformat</code>  does not conform to the International System of Units which recommends using KiB, MiB, GiB, etc. when byte sizes are calculated in powers of 1024 (which is the case here). Instead, Django uses traditional unit names (KB, MB, GB, etc.) corresponding to names that are more commonly used.</p>
<h3 id="first"><code>first</code></h3>
<p>Returns the first item in a list.</p>
<p>For example:</p>
<pre><code>{{ value|first }}
</code></pre>
<p>If  <code>value</code>  is the list  <code>['a', 'b', 'c']</code>, the output will be  <code>'a'</code>.</p>
<h3 id="floatformat"><code>floatformat</code></h3>
<p>When used without an argument, rounds a floating-point number to one decimal place – but only if there’s a decimal part to be displayed. For example:</p>

<table>
<thead>
<tr>
<th><code>value</code></th>
<th>Template</th>
<th>Output</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>34.23234</code></td>
<td><code>{{ value|floatformat }}</code></td>
<td><code>34.2</code></td>
</tr>
<tr>
<td><code>34.00000</code></td>
<td><code>{{ value|floatformat }}</code></td>
<td><code>34</code></td>
</tr>
<tr>
<td><code>34.26000</code></td>
<td><code>{{ value|floatformat }}</code></td>
<td><code>34.3</code></td>
</tr>
</tbody>
</table><p>If used with a numeric integer argument,  <code>floatformat</code>  rounds a number to that many decimal places. For example:</p>

<table>
<thead>
<tr>
<th><code>value</code></th>
<th>Template</th>
<th>Output</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>34.23234</code></td>
<td><code>{{ value|floatformat:3 }}</code></td>
<td><code>34.232</code></td>
</tr>
<tr>
<td><code>34.00000</code></td>
<td><code>{{ value|floatformat:3 }}</code></td>
<td><code>34.000</code></td>
</tr>
<tr>
<td><code>34.26000</code></td>
<td><code>{{ value|floatformat:3 }}</code></td>
<td><code>34.260</code></td>
</tr>
</tbody>
</table><p>Particularly useful is passing 0 (zero) as the argument which will round the float to the nearest integer.</p>

<table>
<thead>
<tr>
<th><code>value</code></th>
<th>Template</th>
<th>Output</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>34.23234</code></td>
<td><code>{{ value|floatformat:"0" }}</code></td>
<td><code>34</code></td>
</tr>
<tr>
<td><code>34.00000</code></td>
<td><code>{{ value|floatformat:"0" }}</code></td>
<td><code>34</code></td>
</tr>
<tr>
<td><code>39.56000</code></td>
<td><code>{{ value|floatformat:"0" }}</code></td>
<td><code>40</code></td>
</tr>
</tbody>
</table><p>If the argument passed to  <code>floatformat</code>  is negative, it will round a number to that many decimal places – but only if there’s a decimal part to be displayed. For example:</p>

<table>
<thead>
<tr>
<th><code>value</code></th>
<th>Template</th>
<th>Output</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>34.23234</code></td>
<td><code>{{ value|floatformat:"-3" }}</code></td>
<td><code>34.232</code></td>
</tr>
<tr>
<td><code>34.00000</code></td>
<td><code>{{ value|floatformat:"-3" }}</code></td>
<td><code>34</code></td>
</tr>
<tr>
<td><code>34.26000</code></td>
<td><code>{{ value|floatformat:"-3" }}</code></td>
<td><code>34.260</code></td>
</tr>
</tbody>
</table><p>Using  <code>floatformat</code>  with no argument is equivalent to using  <code>floatformat</code>  with an argument of  <code>-1</code>.</p>
<p>Changed in Django 3.1:</p>
<p>In older versions, a negative zero  <code>-0</code>  was returned for negative numbers which round to zero.</p>
<h3 id="force_escape"><code>force_escape</code></h3>
<p>Applies HTML escaping to a string (see the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-escape"><code>escape</code></a>  filter for details). This filter is applied  <em>immediately</em>  and returns a new, escaped string. This is useful in the rare cases where you need multiple escaping or want to apply other filters to the escaped results. Normally, you want to use the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-escape"><code>escape</code></a>  filter.</p>
<p>For example, if you want to catch the  <code>&lt;p&gt;</code>  HTML elements created by the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-linebreaks"><code>linebreaks</code></a>  filter:</p>
<pre><code>{% autoescape off %}
    {{ body|linebreaks|force_escape }}
{% endautoescape %}
</code></pre>
<h3 id="get_digit"><code>get_digit</code></h3>
<p>Given a whole number, returns the requested digit, where 1 is the right-most digit, 2 is the second-right-most digit, etc. Returns the original value for invalid input (if input or argument is not an integer, or if argument is less than 1). Otherwise, output is always an integer.</p>
<p>For example:</p>
<pre><code>{{ value|get_digit:"2" }}
</code></pre>
<p>If  <code>value</code>  is  <code>123456789</code>, the output will be  <code>8</code>.</p>
<h3 id="iriencode"><code>iriencode</code></h3>
<p>Converts an IRI (Internationalized Resource Identifier) to a string that is suitable for including in a URL. This is necessary if you’re trying to use strings containing non-ASCII characters in a URL.</p>
<p>It’s safe to use this filter on a string that has already gone through the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-urlencode"><code>urlencode</code></a>  filter.</p>
<p>For example:</p>
<pre><code>{{ value|iriencode }}
</code></pre>
<p>If  <code>value</code>  is  <code>"?test=1&amp;me=2"</code>, the output will be  <code>"?test=1&amp;amp;me=2"</code>.</p>
<h3 id="join"><code>join</code></h3>
<p>Joins a list with a string, like Python’s  <code>str.join(list)</code></p>
<p>For example:</p>
<pre><code>{{ value|join:" // " }}
</code></pre>
<p>If  <code>value</code>  is the list  <code>['a', 'b', 'c']</code>, the output will be the string  <code>"a // b // c"</code>.</p>
<h3 id="json_script"><code>json_script</code></h3>
<p>Safely outputs a Python object as JSON, wrapped in a  <code>&lt;script&gt;</code>  tag, ready for use with JavaScript.</p>
<p><strong>Argument:</strong>  HTML “id” of the  <code>&lt;script&gt;</code>  tag.</p>
<p>For example:</p>
<pre><code>{{ value|json_script:"hello-data" }}
</code></pre>
<p>If  <code>value</code>  is the dictionary  <code>{'hello': 'world'}</code>, the output will be:</p>
<pre><code>&lt;script id="hello-data" type="application/json"&gt;{"hello": "world"}&lt;/script&gt;
</code></pre>
<p>The resulting data can be accessed in JavaScript like this:</p>
<pre><code>const value = JSON.parse(document.getElementById('hello-data').textContent);
</code></pre>
<p>XSS attacks are mitigated by escaping the characters “&lt;”, “&gt;” and “&amp;”. For example if  <code>value</code>  is  <code>{'hello': 'world&lt;/script&gt;&amp;amp;'}</code>, the output is:</p>

<p>This is compatible with a strict Content Security Policy that prohibits in-page script execution. It also maintains a clean separation between passive data and executable code.</p>
<h3 id="last"><code>last</code></h3>
<p>Returns the last item in a list.</p>
<p>For example:</p>
<pre><code>{{ value|last }}
</code></pre>
<p>If  <code>value</code>  is the list  <code>['a', 'b', 'c', 'd']</code>, the output will be the string  <code>"d"</code>.</p>
<h3 id="length"><code>length</code></h3>
<p>Returns the length of the value. This works for both strings and lists.</p>
<p>For example:</p>
<pre><code>{{ value|length }}
</code></pre>
<p>If  <code>value</code>  is  <code>['a', 'b', 'c', 'd']</code>  or  <code>"abcd"</code>, the output will be  <code>4</code>.</p>
<p>The filter returns  <code>0</code>  for an undefined variable.</p>
<h3 id="length_is"><code>length_is</code></h3>
<p>Returns  <code>True</code>  if the value’s length is the argument, or  <code>False</code>  otherwise.</p>
<p>For example:</p>
<pre><code>{{ value|length_is:"4" }}
</code></pre>
<p>If  <code>value</code>  is  <code>['a', 'b', 'c', 'd']</code>  or  <code>"abcd"</code>, the output will be  <code>True</code>.</p>
<h3 id="linebreaks"><code>linebreaks</code></h3>
<p>Replaces line breaks in plain text with appropriate HTML; a single newline becomes an HTML line break (<code>&lt;br&gt;</code>) and a new line followed by a blank line becomes a paragraph break (<code>&lt;/p&gt;</code>).</p>
<p>For example:</p>
<pre><code>{{ value|linebreaks }}
</code></pre>
<p>If  <code>value</code>  is  <code>Joel\nis a slug</code>, the output will be  <code>&lt;p&gt;Joel&lt;br&gt;is a slug&lt;/p&gt;</code>.</p>
<h3 id="linebreaksbr"><code>linebreaksbr</code></h3>
<p>Converts all newlines in a piece of plain text to HTML line breaks (<code>&lt;br&gt;</code>).</p>
<p>For example:</p>
<pre><code>{{ value|linebreaksbr }}
</code></pre>
<p>If  <code>value</code>  is  <code>Joel\nis a slug</code>, the output will be  <code>Joel&lt;br&gt;is a slug</code>.</p>
<h3 id="linenumbers"><code>linenumbers</code></h3>
<p>Displays text with line numbers.</p>
<p>For example:</p>
<pre><code>{{ value|linenumbers }}
</code></pre>
<p>If  <code>value</code>  is:</p>
<pre><code>one
two
three
</code></pre>
<p>the output will be:</p>
<pre><code>1. one
2. two
3. three
</code></pre>
<h3 id="ljust"><code>ljust</code></h3>
<p>Left-aligns the value in a field of a given width.</p>
<p><strong>Argument:</strong>  field size</p>
<p>For example:</p>
<pre><code>"{{ value|ljust:"10" }}"
</code></pre>
<p>If  <code>value</code>  is  <code>Django</code>, the output will be  <code>"Django "</code>.</p>
<h3 id="lower"><code>lower</code></h3>
<p>Converts a string into all lowercase.</p>
<p>For example:</p>
<pre><code>{{ value|lower }}
</code></pre>
<p>If  <code>value</code>  is  <code>Totally LOVING this Album!</code>, the output will be  <code>totally loving this album!</code>.</p>
<h3 id="make_list"><code>make_list</code></h3>
<p>Returns the value turned into a list. For a string, it’s a list of characters. For an integer, the argument is cast to a string before creating a list.</p>
<p>For example:</p>
<pre><code>{{ value|make_list }}
</code></pre>
<p>If  <code>value</code>  is the string  <code>"Joel"</code>, the output would be the list  <code>['J', 'o', 'e', 'l']</code>. If  <code>value</code>  is  <code>123</code>, the output will be the list  <code>['1', '2', '3']</code>.</p>
<h3 id="phone2numeric"><code>phone2numeric</code></h3>
<p>Converts a phone number (possibly containing letters) to its numerical equivalent.</p>
<p>The input doesn’t have to be a valid phone number. This will happily convert any string.</p>
<p>For example:</p>
<p>{{ value|phone2numeric }}</p>
<p>If  <code>value</code>  is  <code>800-COLLECT</code>, the output will be  <code>800-2655328</code>.</p>
<h3 id="pluralize"><code>pluralize</code></h3>
<p>Returns a plural suffix if the value is not  <code>1</code>,  <code>'1'</code>, or an object of length 1. By default, this suffix is  <code>'s'</code>.</p>
<p>Example:</p>
<p>You have {{ num_messages }} message{{ num_messages|pluralize }}.</p>
<p>If  <code>num_messages</code>  is  <code>1</code>, the output will be  <code>You have 1 message.</code>  If  <code>num_messages</code>  is  <code>2</code>  the output will be  <code>You have 2 messages.</code></p>
<p>For words that require a suffix other than  <code>'s'</code>, you can provide an alternate suffix as a parameter to the filter.</p>
<p>Example:</p>
<p>You have {{ num_walruses }} walrus{{ num_walruses|pluralize:“es” }}.</p>
<p>For words that don’t pluralize by simple suffix, you can specify both a singular and plural suffix, separated by a comma.</p>
<p>Example:</p>
<p>You have {{ num_cherries }} cherr{{ num_cherries|pluralize:“y,ies” }}.</p>
<p>Note</p>
<p>Use  <a href="https://docs.djangoproject.com/en/3.1/topics/i18n/translation/#std:templatetag-blocktranslate"><code>blocktranslate</code></a>  to pluralize translated strings.</p>
<h3 id="random"><code>random</code></h3>
<p>Returns a random item from the given list.</p>
<p>For example:</p>
<pre><code>{{ value|random }}
</code></pre>
<p>If  <code>value</code>  is the list  <code>['a', 'b', 'c', 'd']</code>, the output could be  <code>"b"</code>.</p>
<h3 id="rjust"><code>rjust</code></h3>
<p>Right-aligns the value in a field of a given width.</p>
<p><strong>Argument:</strong>  field size</p>
<p>For example:</p>
<pre><code>"{{ value|rjust:"10" }}"
</code></pre>
<p>If  <code>value</code>  is  <code>Django</code>, the output will be  <code>" Django"</code>.</p>
<h3 id="safe"><code>safe</code></h3>
<p>Marks a string as not requiring further HTML escaping prior to output. When autoescaping is off, this filter has no effect.</p>
<p>Note</p>
<p>If you are chaining filters, a filter applied after  <code>safe</code>  can make the contents unsafe again. For example, the following code prints the variable as is, unescaped:</p>
<pre><code>{{ var|safe|escape }}
</code></pre>
<h3 id="safeseq"><code>safeseq</code></h3>
<p>Applies the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-safe"><code>safe</code></a>  filter to each element of a sequence. Useful in conjunction with other filters that operate on sequences, such as  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-join"><code>join</code></a>. For example:</p>
<pre><code>{{ some_list|safeseq|join:", " }}
</code></pre>
<p>You couldn’t use the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-safe"><code>safe</code></a>  filter directly in this case, as it would first convert the variable into a string, rather than working with the individual elements of the sequence.</p>
<h3 id="slice"><code>slice</code></h3>
<p>Returns a slice of the list.</p>
<p>Uses the same syntax as Python’s list slicing. See  <a href="https://www.diveinto.org/python3/native-datatypes.html#slicinglists">https://www.diveinto.org/python3/native-datatypes.html#slicinglists</a>  for an introduction.</p>
<p>Example:</p>
<pre><code>{{ some_list|slice:":2" }}
</code></pre>
<p>If  <code>some_list</code>  is  <code>['a', 'b', 'c']</code>, the output will be  <code>['a', 'b']</code>.</p>
<h3 id="slugify"><code>slugify</code></h3>
<p>Converts to ASCII. Converts spaces to hyphens. Removes characters that aren’t alphanumerics, underscores, or hyphens. Converts to lowercase. Also strips leading and trailing whitespace.</p>
<p>For example:</p>
<pre><code>{{ value|slugify }}
</code></pre>
<p>If  <code>value</code>  is  <code>"Joel is a slug"</code>, the output will be  <code>"joel-is-a-slug"</code>.</p>
<h3 id="stringformat"><code>stringformat</code></h3>
<p>Formats the variable according to the argument, a string formatting specifier. This specifier uses the  <a href="https://docs.python.org/3/library/stdtypes.html#old-string-formatting" title="(in Python v3.9)">printf-style String Formatting</a>  syntax, with the exception that the leading “%” is dropped.</p>
<p>For example:</p>
<pre><code>{{ value|stringformat:"E" }}
</code></pre>
<p>If  <code>value</code>  is  <code>10</code>, the output will be  <code>1.000000E+01</code>.</p>
<h3 id="striptags"><code>striptags</code></h3>
<p>Makes all possible efforts to strip all [X]HTML tags.</p>
<p>For example:</p>
<pre><code>{{ value|striptags }}
</code></pre>
<p>If  <code>value</code>  is  <code>"&lt;b&gt;Joel&lt;/b&gt; &lt;button&gt;is&lt;/button&gt; a &lt;span&gt;slug&lt;/span&gt;"</code>, the output will be  <code>"Joel is a slug"</code>.</p>
<p>No safety guarantee</p>
<p>Note that  <code>striptags</code>  doesn’t give any guarantee about its output being HTML safe, particularly with non valid HTML input. So  <strong>NEVER</strong>  apply the  <code>safe</code>  filter to a  <code>striptags</code>  output. If you are looking for something more robust, you can use the  <code>bleach</code>  Python library, notably its  <a href="https://bleach.readthedocs.io/en/latest/clean.html">clean</a>  method.</p>
<h3 id="time"><code>time</code></h3>
<p>Formats a time according to the given format.</p>
<p>Given format can be the predefined one  <a href="https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-TIME_FORMAT"><code>TIME_FORMAT</code></a>, or a custom format, same as the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-date"><code>date</code></a>  filter. Note that the predefined format is locale-dependent.</p>
<p>For example:</p>
<pre><code>{{ value|time:"H:i" }}
</code></pre>
<p>If  <code>value</code>  is equivalent to  <code>datetime.datetime.now()</code>, the output will be the string  <code>"01:23"</code>.</p>
<p>Note that you can backslash-escape a format string if you want to use the “raw” value. In this example, both “h” and “m” are backslash-escaped, because otherwise each is a format string that displays the hour and the month, respectively:</p>
<pre><code>{% value|time:"H\h i\m" %}
</code></pre>
<p>This would display as <code>“01h 23m”.</code></p>
<p>Another example:</p>
<p>Assuming that  <a href="https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-USE_L10N"><code>USE_L10N</code></a>  is  <code>True</code>  and  <a href="https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-LANGUAGE_CODE"><code>LANGUAGE_CODE</code></a>  is, for example,  <code>"de"</code>, then for:</p>
<pre><code>{{ value|time:"TIME_FORMAT" }}
</code></pre>
<p>the output will be the string  <code>"01:23"</code>  (The  <code>"TIME_FORMAT"</code>  format specifier for the  <code>de</code>  locale as shipped with Django is  <code>"H:i"</code>).</p>
<p>The  <code>time</code>  filter will only accept parameters in the format string that relate to the time of day, not the date. If you need to format a  <code>date</code>  value, use the  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-date"><code>date</code></a>  filter instead (or along with  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-time"><code>time</code></a>  if you need to render a full  <a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.9)"><code>datetime</code></a>  value).</p>
<p>There is one exception the above rule: When passed a  <code>datetime</code>  value with attached timezone information (a  <a href="https://docs.djangoproject.com/en/3.1/topics/i18n/timezones/#naive-vs-aware-datetimes">time-zone-aware</a>  <code>datetime</code>  instance) the  <code>time</code>  filter will accept the timezone-related  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#date-and-time-formatting-specifiers">format specifiers</a>  <code>'e'</code>,  <code>'O'</code>  ,  <code>'T'</code>  and  <code>'Z'</code>.</p>
<p>When used without a format string, the  <code>TIME_FORMAT</code>  format specifier is used:</p>
<pre><code>{{ value|time }}
</code></pre>
<p>is the same as:</p>
<pre><code>{{ value|time:"TIME_FORMAT" }}
</code></pre>
<h3 id="timesince"><code>timesince</code></h3>
<p>Formats a date as the time since that date (e.g., “4 days, 6 hours”).</p>
<p>Takes an optional argument that is a variable containing the date to use as the comparison point (without the argument, the comparison point is  <em>now</em>). For example, if  <code>blog_date</code>  is a date instance representing midnight on 1 June 2006, and  <code>comment_date</code>  is a date instance for 08:00 on 1 June 2006, then the following would return “8 hours”:</p>
<pre><code>{{ blog_date|timesince:comment_date }}
</code></pre>
<p>Comparing offset-naive and offset-aware datetimes will return an empty string.</p>
<p>Minutes is the smallest unit used, and “0 minutes” will be returned for any date that is in the future relative to the comparison point.</p>
<h3 id="timeuntil"><code>timeuntil</code></h3>
<p>Similar to  <code>timesince</code>, except that it measures the time from now until the given date or datetime. For example, if today is 1 June 2006 and  <code>conference_date</code>  is a date instance holding 29 June 2006, then  <code>{{ conference_date|timeuntil }}</code>  will return “4 weeks”.</p>
<p>Takes an optional argument that is a variable containing the date to use as the comparison point (instead of  <em>now</em>). If  <code>from_date</code>  contains 22 June 2006, then the following will return “1 week”:</p>
<pre><code>{{ conference_date|timeuntil:from_date }}
</code></pre>
<p>Comparing offset-naive and offset-aware datetimes will return an empty string.</p>
<p>Minutes is the smallest unit used, and “0 minutes” will be returned for any date that is in the past relative to the comparison point.</p>
<h3 id="title"><code>title</code></h3>
<p>Converts a string into titlecase by making words start with an uppercase character and the remaining characters lowercase. This tag makes no effort to keep “trivial words” in lowercase.</p>
<p>For example:</p>
<pre><code>{{ value|title }}
</code></pre>
<p>If  <code>value</code>  is  <code>"my FIRST post"</code>, the output will be  <code>"My First Post"</code>.</p>
<h3 id="truncatechars"><code>truncatechars</code></h3>
<p>Truncates a string if it is longer than the specified number of characters. Truncated strings will end with a translatable ellipsis character (“…”).</p>
<p><strong>Argument:</strong>  Number of characters to truncate to</p>
<p>For example:</p>
<pre><code>{{ value|truncatechars:7 }}
</code></pre>
<p>If  <code>value</code>  is  <code>"Joel is a slug"</code>, the output will be  <code>"Joel i…"</code>.</p>
<h3 id="truncatechars_html"><code>truncatechars_html</code></h3>
<p>Similar to  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-truncatechars"><code>truncatechars</code></a>, except that it is aware of HTML tags. Any tags that are opened in the string and not closed before the truncation point are closed immediately after the truncation.</p>
<p>For example:</p>
<pre><code>{{ value|truncatechars_html:7 }}
</code></pre>
<p>If  <code>value</code>  is  <code>"&lt;p&gt;Joel is a slug&lt;/p&gt;"</code>, the output will be  <code>"&lt;p&gt;Joel i…&lt;/p&gt;"</code>.</p>
<p>Newlines in the HTML content will be preserved.</p>
<h3 id="truncatewords"><code>truncatewords</code></h3>
<p>Truncates a string after a certain number of words.</p>
<p><strong>Argument:</strong>  Number of words to truncate after</p>
<p>For example:</p>
<pre><code>{{ value|truncatewords:2 }}
</code></pre>
<p>If  <code>value</code>  is  <code>"Joel is a slug"</code>, the output will be  <code>"Joel is …"</code>.</p>
<p>Newlines within the string will be removed.</p>
<h3 id="truncatewords_html"><code>truncatewords_html</code></h3>
<p>Similar to  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-truncatewords"><code>truncatewords</code></a>, except that it is aware of HTML tags. Any tags that are opened in the string and not closed before the truncation point, are closed immediately after the truncation.</p>
<p>This is less efficient than  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-truncatewords"><code>truncatewords</code></a>, so should only be used when it is being passed HTML text.</p>
<p>For example:</p>
<pre><code>{{ value|truncatewords_html:2 }}
</code></pre>
<p>If  <code>value</code>  is  <code>"&lt;p&gt;Joel is a slug&lt;/p&gt;"</code>, the output will be  <code>"&lt;p&gt;Joel is …&lt;/p&gt;"</code>.</p>
<p>Newlines in the HTML content will be preserved.</p>
<h3 id="unordered_list"><code>unordered_list</code></h3>
<p>Recursively takes a self-nested list and returns an HTML unordered list – WITHOUT opening and closing </p><ul> tags.</ul><p></p>
<p>The list is assumed to be in the proper format. For example, if  <code>var</code>  contains  <code>['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']]</code>, then  <code>{{ var|unordered_list }}</code>  would return:</p>
<pre><code>&lt;li&gt;States
&lt;ul&gt;
     &lt;li&gt;Kansas
     &lt;ul&gt;
         &lt;li&gt;Lawrence&lt;/li&gt;
         &lt;li&gt;Topeka&lt;/li&gt;
     &lt;/ul&gt;
     &lt;/li&gt;
     &lt;li&gt;Illinois&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
</code></pre>
<h3 id="upper"><code>upper</code></h3>
<p>Converts a string into all uppercase.</p>
<p>For example:</p>
<pre><code>{{ value|upper }}
</code></pre>
<p>If  <code>value</code>  is  <code>"Joel is a slug"</code>, the output will be  <code>"JOEL IS A SLUG"</code>.</p>
<h3 id="urlencode"><code>urlencode</code></h3>
<p>Escapes a value for use in a URL.</p>
<p>For example:</p>
<pre><code>{{ value|urlencode }}
</code></pre>
<p>If  <code>value</code>  is  <code>"https://www.example.org/foo?a=b&amp;c=d"</code>, the output will be  <code>"https%3A//www.example.org/foo%3Fa%3Db%26c%3Dd"</code>.</p>
<p>An optional argument containing the characters which should not be escaped can be provided.</p>
<p>If not provided, the ‘/’ character is assumed safe. An empty string can be provided when  <em>all</em>  characters should be escaped. For example:</p>
<pre><code>{{ value|urlencode:"" }}
</code></pre>
<p>If  <code>value</code>  is  <code>"https://www.example.org/"</code>, the output will be  <code>"https%3A%2F%2Fwww.example.org%2F"</code>.</p>
<h3 id="urlize"><code>urlize</code></h3>
<p>Converts URLs and email addresses in text into clickable links.</p>
<p>This template tag works on links prefixed with  <code>http://</code>,  <code>https://</code>, or  <code>www.</code>. For example,  <code>https://goo.gl/aia1t</code>  will get converted but  <code>goo.gl/aia1t</code>  won’t.</p>
<p>It also supports domain-only links ending in one of the original top level domains (<code>.com</code>,  <code>.edu</code>,  <code>.gov</code>,  <code>.int</code>,  <code>.mil</code>,  <code>.net</code>, and  <code>.org</code>). For example,  <code>djangoproject.com</code>  gets converted.</p>
<p>Links can have trailing punctuation (periods, commas, close-parens) and leading punctuation (opening parens), and  <code>urlize</code>  will still do the right thing.</p>
<p>Links generated by  <code>urlize</code>  have a  <code>rel="nofollow"</code>  attribute added to them.</p>
<p>For example:</p>
<pre><code>{{ value|urlize }}
</code></pre>
<p>If  <code>value</code>  is  <code>"Check out www.djangoproject.com"</code>, the output will be  <code>"Check out &lt;a href="http://www.djangoproject.com" rel="nofollow"&gt;www.djangoproject.com&lt;/a&gt;"</code>.</p>
<p>In addition to web links,  <code>urlize</code>  also converts email addresses into  <code>mailto:</code>  links. If  <code>value</code>  is  <code>"Send questions to foo@example.com"</code>, the output will be  <code>"Send questions to &lt;a href="mailto:foo@example.com"&gt;foo@example.com&lt;/a&gt;"</code>.</p>
<p>The  <code>urlize</code>  filter also takes an optional parameter  <code>autoescape</code>. If  <code>autoescape</code>  is  <code>True</code>, the link text and URLs will be escaped using Django’s built-in  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatefilter-escape"><code>escape</code></a>  filter. The default value for  <code>autoescape</code>  is  <code>True</code>.</p>
<blockquote>
<p><em>Note</em><br>
<em>If  <code>urlize</code>  is applied to text that already contains HTML markup, or to email addresses that contain single quotes (<code>'</code>), things won’t work as expected. Apply this filter only to plain text.</em></p>
</blockquote>
<h3 id="urlizetrunc"><code>urlizetrunc</code></h3>
<p>Converts URLs and email addresses into clickable links just like  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#urlize">urlize</a>, but truncates URLs longer than the given character limit.</p>
<p><strong>Argument:</strong>  Number of characters that link text should be truncated to, including the ellipsis that’s added if truncation is necessary.</p>
<p>For example:</p>
<pre><code>{{ value|urlizetrunc:15 }}
</code></pre>
<p>If  <code>value</code>  is  <code>"Check out www.djangoproject.com"</code>, the output would be  <code>'Check out &lt;a href="http://www.djangoproject.com" rel="nofollow"&gt;www.djangoproj…&lt;/a&gt;'</code>.</p>
<p>As with  <a href="https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#urlize">urlize</a>, this filter should only be applied to plain text.</p>
<h3 id="wordcount"><code>wordcount</code></h3>
<p>Returns the number of words.</p>
<p>For example:</p>
<pre><code>{{ value|wordcount }}
</code></pre>
<p>If  <code>value</code>  is  <code>"Joel is a slug"</code>, the output will be  <code>4</code>.</p>
<h3 id="wordwrap"><code>wordwrap</code></h3>
<p>Wraps words at specified line length.</p>
<p><strong>Argument:</strong>  number of characters at which to wrap the text</p>
<p>For example:</p>
<pre><code>{{ value|wordwrap:5 }}
</code></pre>
<p>If  <code>value</code>  is  <code>Joel is a slug</code>, the output would be:</p>
<pre><code>Joel
is a
slug
</code></pre>

