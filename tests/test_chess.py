from unittest import mock

import pytest

from chess.chess import (
    Board,
    ImpossibleSettle,
    # Rook,
)


class TestBoard:

    class TestSettle:

        def test_it_should_settle_a_rook_in_a_square(self):
            board = Board()
            rook = mock.Mock()

            board.settle(rook, x='a', y='1')

            assert board.squares['a']['1'] == rook

        def test_it_should_fail_on_out_of_x_axis(self):
            board = Board()
            rook = mock.Mock()

            with pytest.raises(ImpossibleSettle):
                board.settle(rook, x='z', y='1')

        def test_it_should_fail_on_out_of_y_axis(self):
            board = Board()
            rook = mock.Mock()

            with pytest.raises(ImpossibleSettle):
                board.settle(rook, x='a', y='9')

        def test_it_should_fail_a_rook_in_another_rook(self):
            board = Board()
            rook1 = mock.Mock()
            rook2 = mock.Mock()

            board.settle(rook1, x='a', y='1')
            with pytest.raises(ImpossibleSettle):
                board.settle(rook2, x='a', y='1')
