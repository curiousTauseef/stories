# -*- coding: utf-8 -*-
import pytest


@pytest.mark.xfail
def test_contrib_is_available():
    from stories.contrib.debug_toolbars.flask import StoriesPanel  # noqa: F401
