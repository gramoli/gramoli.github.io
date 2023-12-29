---
layout: default
author: Vincent Gramoli
title: Blog - Thinking Distributed 
description: This blog aims at being thought provoking and covers subjects related to the distributed nature of blockchain systems.
permalink: /blog/
author_profile: false
---
<h1>Latest Posts</h1>

<ul>
  {% for post in site.posts %}
    <li>
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      {{ post.excerpt - post.tags }}
    </li>
  {% endfor %}
</ul>

<h1>Tags</h1>
<ul>
{% for tag in site.tags %}
  <li>
  {{ tag[0] }}:
    {% for post in tag[1] %}
      <a href="{{ post.url }}">{{ post.title }}</a>&nbsp;
    {% endfor %}
  </li>
{% endfor %}
</ul>
