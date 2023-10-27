from symbiot_lib.objects.step_record import StepRecord


class CalibrationHandler:

    def create(self, wish):
        print("service, create: " + wish)

        operation = Operation(wish)
        operation.status = "CALIBRATION"
        step_1 = StepRecord([])

        operation.add_record(step_1)
        self._repository.save(operation)

        self.mediator("client").calibrate(step_1, wish)
