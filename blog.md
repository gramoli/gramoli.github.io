---
layout: default
author: Vincent Gramoli
title: Blog - Thinking Distributed 
description: This blog aims at being thought provoking and covers subjects related to the distributed nature of blockchain systems.
permalink: /blog/
author_profile: false
---
[Home](../index) | [Research](../research) | [Software](../software) | [Publications](../publications) | [Blog](blog)

<h1>Blog - Thinking Distributed</h1>

<h2>Latest Posts</h2>
<ul>
  {% for post in site.posts %}
    <li>
      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
      {{ post.excerpt - post.tags }}
    </li>
  {% endfor %}
</ul>

<h2>Tags</h2>
<ul>
{% for tag in site.tags %}
  <li>
  {{ tag[0] }}
    {% for post in tag[1] %}
      <a href="{{ post.url }}">{{ post.title }}</a>&nbsp;
    {% endfor %}
  </li>
{% endfor %}
</ul>
