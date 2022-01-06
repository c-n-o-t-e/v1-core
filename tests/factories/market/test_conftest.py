def test_factory_fixture(factory, feed_factory, ovl, gov):
    # check params set properly
    assert factory.ovl() == ovl

    # check appropriate factory roles given to contract deployer
    assert factory.hasRole(factory.ADMIN_ROLE(), gov) is True
    assert factory.hasRole(factory.GOVERNOR_ROLE(), gov) is True

    # check factory has been given admin role on ovl token
    assert ovl.hasRole(ovl.ADMIN_ROLE(), factory) is True

    # check feed factory has been added to registry
    assert factory.isFeedFactory(feed_factory) is True


def test_feed_factory_fixture(feed_factory, feed_one, feed_two, feed_three):
    # check params set properly
    feed_factory.microWindow() == 600
    feed_factory.macroWindow() == 3600

    # check feeds with (price, reserve) combos have been deployed
    assert feed_factory.isFeed(feed_one) is True
    assert feed_factory.isFeed(feed_two) is True
    assert feed_factory.isFeed(feed_three) is True


def test_market_fixture(market, factory, feed_three, ovl, gov):
    # check params set properly
    # NOTE: market fixture uses feed three
    assert market.ovl() == ovl
    assert market.factory() == factory
    assert market.feed() == feed_three

    assert market.k() == 1220000000000
    assert market.lmbda() == 1000000000000000000
    assert market.delta() == 2500000000000000
    assert market.capPayoff() == 5000000000000000000
    assert market.capOi() == 800000000000000000000000
    assert market.capLeverage() == 5000000000000000000
    assert market.maintenanceMargin() == 100000000000000000
    assert market.maintenanceMarginBurnRate() == 100000000000000000
    assert market.tradingFeeRate() == 750000000000000
    assert market.minCollateral() == 100000000000000

    assert market.tradingFeeRecipient() == factory
