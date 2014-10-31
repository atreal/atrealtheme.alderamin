# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from atrealtheme.alderamin.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of atrealtheme.alderamin into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if atrealtheme.alderamin is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('atrealtheme.alderamin'))

    def test_uninstall(self):
        """Test if atrealtheme.alderamin is cleanly uninstalled."""
        self.installer.uninstallProducts(['atrealtheme.alderamin'])
        self.assertFalse(self.installer.isProductInstalled('atrealtheme.alderamin'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IAtrealthemeAlderaminLayer is registered."""
        from atrealtheme.alderamin.interfaces import IAtrealthemeAlderaminLayer
        from plone.browserlayer import utils
        self.failUnless(IAtrealthemeAlderaminLayer in utils.registered_layers())
