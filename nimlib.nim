import httpclient
import nimpy


proc get(url: string): string {.exportpy.} =
  return newHttpClient().getContent(url)
