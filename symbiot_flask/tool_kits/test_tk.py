from tool_kits.tool_kit import ToolKit


class TestTK(ToolKit):
    @ToolKit.tool_function(
        description="method just printing log with the input",
        parameters=[dict(
            name="arg",
            type="string",
            description="just some string to be printed"
        )]
    )
    def method(self, arg):
        print(f"success: {arg}")
