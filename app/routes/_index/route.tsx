import { Link } from "@remix-run/react"
import { selectEnv } from "~/lib/navlinkVariables"

export default function LandingPage() {
  return <>
    <div className="flex flex-row h-screen w-screen">
      <div className="basis-1/2 content-center h-full">

        <div className="hero">
          <div className="flex text-[128px] justify-center leading-tight">Coordinate</div>
          <div className="flex justify-center text-4xl leading-3">Build and execute distributed workloads with GUI</div>
        </div>

        <div className="links">
          <Link to={selectEnv}><div className="text-3xl flex justify-center mt-20 my-5">Build Now</div></Link>
          <div className="text-3xl flex justify-center my-5">Docs</div>
          <div className="text-3xl flex justify-center my-5">Downloadables</div>
          <div className="text-3xl flex justify-center my-5">Github</div>
        </div>

      </div>
      <div className="flex basis-1/2 justify-center items-center text-4xl">TODO: Image</div>
    </div>
  </>
}