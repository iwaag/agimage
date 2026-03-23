from hatchet_sdk import DurableContext, Hatchet
from agpyutils.task import models

hatchet = Hatchet()


@hatchet.durable_task(name="image_gen", input_validator=models.Task_UnmanagedLabor)
async def task_image_gen(input: models.Task_UnmanagedLabor, context: DurableContext) -> dict[str, str]:
    del input
    del context
    return {"status": "accepted"}
