import os
from fastmcp import FastMCP

# 환경 변수(FASTMCP_SERVER_AUTH)를 통해 GoogleProvider가 자동 설정됩니다.
mcp = FastMCP(name="Railway Google OAuth Test")

# ---------------------------------------------------------
# 👇 여기 추가된 더하기 도구입니다
@mcp.tool
async def add(a: int, b: int) -> int:
    """두 숫자를 더합니다. (Google 로그인 필요)"""
    return a + b
# ---------------------------------------------------------

@mcp.tool
async def get_my_info() -> dict:
    """로그인된 사용자의 정보를 반환합니다."""
    from fastmcp.server.dependencies import get_access_token
    
    token = get_access_token()
    
    return {
        "status": "Authenticated",
        "email": token.claims.get("email"),
        "name": token.claims.get("name")
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    mcp.run(transport="http", host="0.0.0.0", port=port)
