import sys
from flask import render_template, redirect, url_for, request, abort
from app.models.Group import Group

def index():
  return Group.query.all()


def store():
  return {}


def show(id):
  # TODO: Use actual arguments
  return Group.filter(1==1).all().serialize()


def update(id):
  return {}


def delete(id):
  return {}