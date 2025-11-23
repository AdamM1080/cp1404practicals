from unreliable_car import UnreliableCar


def main():
    """Run basic stochastic tests for UnreliableCar."""

    test_drive_attempts(30, 100)
    test_drive_attempts(80, 100)
    test_drive_attempts(0, 50)
    test_drive_attempts(100, 50)


def test_drive_attempts(reliability, trials):
    """Test that the number of successful drives is reasonable."""
    print(f"\nTesting {reliability}% reliable car over {trials} attempts")

    car = UnreliableCar("TestCar", 10000, reliability)
    successes = 0

    for _ in range(trials):
        distance_driven = car.drive(1)
        if distance_driven > 0:
            successes += 1

    print(f"Successful drives: {successes}/{trials}")

    expected = trials * (reliability / 100)
    lower = expected * 0.5
    upper = expected * 1.5

    if lower < successes < upper:
        print("PASS: Success rate is within reasonable bounds.")
    else:
        print("FAIL: Success rate is outside expected range.")


if __name__ == "__main__":
    main()